# Copyright 2020 Grid AI Inc.
import ast
import asyncio
import base64
import csv
from datetime import datetime
import json
import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from urllib.parse import urljoin, urlsplit

import click
from dateutil.parser import parse as date_string_parse
from gql import Client, gql
from gql.transport.exceptions import TransportProtocolError, TransportQueryError
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.websockets import WebsocketsTransport
import humanize
from packaging import version
import requests
from requests.exceptions import HTTPError
from rich.console import Console
import websockets
import yaml
import yaspin

from grid.commands import CredentialsMixin, DependencyMixin, WorkflowChecksMixin
from grid.commands.git import execute_git_command
from grid.datastore import create_datastore_session, DatastoreUploadSession
from grid.exceptions import AuthenticationError, TrainError
import grid.globals as env
from grid.metadata import __version__
from grid.observables import BaseObservable, Experiment, InteractiveNode, Run
from grid.types import ObservableType, WorkflowType

_graphql_client: Client = None

CREDIT_CARD_ERROR_MESSAGE = "A credit card on file is needed in order to use a GPU"


class Grid(CredentialsMixin, WorkflowChecksMixin, DependencyMixin):
    """
    Interface to the Grid API.

    Attributes
    ----------
    url: str
        Grid URL
    request_timeout: int
        Number of seconds to timeout a request by default.
    client: Client
        gql client object
    grid_credentials_path: str
        Path to the Grid credentials
    default_headers: Dict[str, str]
        Header used in the request made to Grid.
    acceptable_lines_to_print: int
        Total number of acceptable lines to print in
        stdout.
    request_cooldown_duration: float
        Number of seconds to wait between continuous
        requests.

    Parameters
    ----------
    local_credentials: bool, default True
        If the client should be initialized with
        credentials from a local file or not.
    """
    url: str = env.GRID_URL

    #  TODO: Figure out a better timeout based on query type.
    request_timeout: int = 60
    default_headers: Dict[str, str] = {'Content-type': 'application/json', 'User-Agent': f'grid-api-{__version__}'}

    grid_settings_path: str = '.grid/settings.json'
    grid_credentials_path: str = '.grid/credentials.json'

    client: Client
    transport: RequestsHTTPTransport

    available_observables: Dict[ObservableType, Callable] = {
        ObservableType.EXPERIMENT: Experiment,
        ObservableType.RUN: Run,
        ObservableType.INTERACTIVE: InteractiveNode
    }

    acceptable_lines_to_print: int = 50
    request_cooldown_duration: int = 0.1

    def __init__(self, credential_path: Optional[str] = None, load_local_credentials: bool = True):

        self.credentials: Dict[str, str] = {}
        self.credential_path = credential_path
        self.headers = self.default_headers.copy()

        #  By default, we instantiate the client with a local
        #  set of credentials.
        if load_local_credentials or self.credential_path:
            self._set_local_credentials()

            #  The client will be created with a set of credentials.
            #  If we change these credentials in the context of a
            #  call, for instance "login()" then we have to
            #  re-instantiate these credentials.
            self._init_client()

        # Loads global settings on startup.
        # Also creates settings if they are not
        # available.
        self._load_global_settings()
        super().__init__()

    @property
    def user_id(self):
        return self.credentials.get('UserID')

    def _set_local_credentials(self):
        """
        Instantiates the GraphQL local client using local credentials.
        """
        #  Re-fetches values from env.
        env.USER_ID = os.getenv('GRID_USER_ID')
        env.API_KEY = os.getenv('GRID_API_KEY')
        if env.USER_ID and env.API_KEY:
            click.echo('Configuring user from environment')
            self.__set_authentication_headers(username=env.USER_ID, key=env.API_KEY)
            return

        #  Checks if the environment variable GRID_CREDENTIAL_PATH
        #  contains a path for grid credentials.
        #  TODO: Click has a better interface for doing this.
        env_path = os.getenv('GRID_CREDENTIAL_PATH')
        if env_path:
            P = Path(env_path)
            if not P.exists():
                m = f'Credentials not found at {env_path}. Did you set GRID_CREDENTIAL_PATH correctly?'
                raise click.ClickException(m)
        elif self.credential_path:
            P = Path(self.credential_path)
            if not P.exists():
                m = f'Credentials not found at {self.credential_path}'
                raise click.ClickException(m)
        else:
            P = Path.home().joinpath(self.grid_credentials_path)

        if P.exists():
            self.credentials = json.load(P.open())
            self.__set_authentication_headers(username=self.credentials['UserID'], key=self.credentials['APIKey'])

        else:
            raise click.ClickException('No credentials available. Did you login?')

    def __set_authentication_headers(self, username: str, key: str) -> None:
        """
        Sets credentials header for a client.
        """
        self.headers['X-Grid-User'] = username
        self.headers['X-Grid-Key'] = key

    def _load_global_settings(self) -> None:
        """
        Loads user settings and sets them globally
        in the Client context.
        """
        P = Path.home().joinpath(self.grid_settings_path)

        # Make sure path exists.
        Path(P.parents[0]).mkdir(parents=True, exist_ok=True)

        # If file doesn't exist, create with default global
        # settings.
        if not P.exists():
            global_variables = {'debug': False, 'ignore_warnings': False, 'skip_vesion_check': False}
            with P.open('w') as file:
                json.dump(global_variables, file, ensure_ascii=False, indent=4)

        # Setup settings based on what the user has
        # configured.
        else:
            user_settings = json.load(P.open())
            if 'debug' in user_settings and env.DEBUG is None:
                env.DEBUG = bool(user_settings['debug'])

            if 'ignore_warnings' in user_settings and env.IGNORE_WARNINGS is None:
                env.IGNORE_WARNINGS = bool(user_settings['ignore_warnings'])

            if 'skip_version_check' in user_settings and env.SKIP_VERSION_CHECK is None:
                env.SKIP_VERSION_CHECK = bool(user_settings['skip_vesion_check'])

    def _check_version_compatibility(self):
        """
        Checks API version compatibility between server and client.
        Raises exception if versions are incompatible.
        """
        # Skip version check if configured by user.
        if env.SKIP_VERSION_CHECK:
            return

        _url = self.url.replace('graphql', '')
        _url = urljoin(_url, 'metadata')
        response = requests.get(_url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise click.ClickException('Grid is currently unavailable. ' 'Try again in a few minutes.')

        data = response.json()
        server_version = data['version']

        # Compare versions.
        message = """You need to update Grid! Please Run:

    pip install lightning-grid --upgrade
"""
        grid_version = version.parse(server_version)
        client_version = version.parse(__version__)

        # Right now any version differences will
        # raise an exception. We can be a lot more detailed
        # in the future and only error on major differences.
        if grid_version > client_version:
            if grid_version.major > client_version.major:
                click.echo(message)
                raise click.ClickException(
                    'Incompatible versions: {grid_version} (server) and '
                    '{client_version} (client)'
                )

    def _init_client(self, websocket: bool = False) -> None:
        """
        Initializes GraphQL client. This fetches the latest
        schema from Grid.
        """
        # Check version compatibility on client initialization.
        # TODO re-enable when versioning is fixed
        # self._check_version_compatibility()

        if websocket:
            _url = self.url.replace('http://', 'ws://')
            _url = _url.replace('https://', 'wss://')
            _url = _url.replace('graphql', 'subscriptions')
            self.transport = WebsocketsTransport(url=_url, init_payload=self.headers)
        else:
            self.transport = RequestsHTTPTransport(
                url=self.url, use_json=True, headers=self.headers, timeout=self.request_timeout, retries=3
            )

        try:
            # Only create a client instance if there isn't one.
            # We also check if the instantiated transport is different.
            # We'll create a new client if it is.
            global _graphql_client
            if not isinstance(_graphql_client, Client) or _graphql_client.transport != self.transport:
                _graphql_client = Client(transport=self.transport, fetch_schema_from_transport=True)

            self.client = _graphql_client

        except requests.exceptions.ConnectionError:
            raise click.ClickException(
                f'Grid is unreachable. Is Grid online at {env.GRID_URL.replace("/graphql", "")} ?'
            )
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise click.ClickException('Not authorized. Did you login?')
            if e.response.status_code == 500:
                raise click.ClickException('Grid is having issues. Please again later.')
            raise click.ClickException('We encountered an unknown error.')

        except requests.exceptions.Timeout:
            raise click.ClickException('Could not reach Grid. Are you online?')

        except TransportProtocolError:
            raise click.ClickException('Not authorized. Did you login?')

        except Exception as e:
            raise click.ClickException(f"{type(e).__name__}: {e}")

    def query(self, query: str, **kwargs) -> Dict:
        """Executes a GraphQL query against Grid's API."""
        # instantiate http transport
        if not hasattr(self, "transport") or not isinstance(self.transport, RequestsHTTPTransport):
            self._init_client(websocket=False)

        values = kwargs or {}
        try:
            result = self.client.execute(gql(query), variable_values=values)
        except TransportQueryError as e:
            raise click.ClickException(e.args)
        except Exception as e:
            raise click.ClickException(f"{type(e).__name__}: {e}")
        if 'error' in result:
            raise click.ClickException(json.dumps(result['error']))
        return result

    def mutate(self, query: str, **kwargs) -> Dict:
        """Executes a GraphQL mutation against Grid's API."""
        return self.query(query, **kwargs)

    def subscribe(self, query: str, **kwargs) -> Dict:
        """Streams data from a GraphQL subscription"""
        # instantiate a websocket transport
        if not hasattr(self, "transport") or not isinstance(self.transport, WebsocketsTransport):
            self._init_client(websocket=True)

        values = kwargs or {}
        try:
            stream = self.client.subscribe(gql(query), variable_values=values)
            for element in stream:
                yield element

        # If connection is suddenly closed, indicate that a known
        # error happened.
        except websockets.exceptions.ConnectionClosedError:
            raise click.ClickException('Could not fetch log data.')

        except websockets.exceptions.ConnectionClosedOK:
            raise click.ClickException('Could not continue fetching log stream.')

        except asyncio.exceptions.TimeoutError:
            raise click.ClickException('Timeout waiting for messages exceeded.')

        #  Raise any other errors that the backend may raise.
        except Exception as e:  # skipcq: PYL-W0703
            raise click.ClickException(str(e))

    @staticmethod
    def _add_git_root_path(entrypoint: str) -> str:
        #  Finds the relative path of the file to train.
        script_path = Path(entrypoint).absolute()
        repository_path = execute_git_command(['rev-parse', '--show-toplevel'], cwd=script_path)
        return str(script_path.relative_to(repository_path))

    def _check_user_github_token(self) -> bool:
        """
        Checks if user has a valid Github token available.
        If user doesn't have one, then redirect user to the
        Grid UI to fetch a new one.

        Returns
        -------
        has_token: bool
            Boolean indicating if user has valid token.
        """
        # Build query
        query = gql(
            """
            query CheckToken {
                checkUserGithubToken {
                    hasValidToken
                }
            }
        """
        )

        # Check if the user has a token. If she hasn't,
        # then redirect user to the /auth page to get a new
        # Github token.
        has_token = False
        try:
            result = self.client.execute(query)
            has_token = result['checkUserGithubToken']['hasValidToken']
            if not has_token:
                auth_url = env.GRID_URL.replace("graphql", "auth")
                click.launch(auth_url)
                raise click.ClickException(
                    """
    Authentication tokens need to be renewed! Opening Grid on the browser so
    we can renew your authentication tokens.
    """
                )

        except HTTPError as e:
            click.echo(str(e), err=True)
            raise AuthenticationError(e)

        return has_token

    def _check_github_repo_accessible(self, github_repository: str) -> bool:
        """
        Checks if user has authoirized Grid to access a given Github repository.
        If the user did not, then redirect them to the
        Grid UI settings page to authorize.

        Parameters
        ----------
        github_repository: str
            Github repository URL or ID

        Returns
        -------
        is_accessible: bool
            Boolean indicating if the user authorized to access the Github repository,
        """
        result = self.client.execute(
            gql(
                """
            query ($repositoryUrl: ID!) {
                isGithubRepositoryAccessible(repositoryUrl: $repositoryUrl) {
                    isAccessible
                }
            }"""
            ),
            variable_values={'repositoryUrl': github_repository}
        )

        return result['isGithubRepositoryAccessible']['isAccessible']

    def login(self, username: str, key: str):
        """
        Logs into grid, creating a local credential set.

        Parameters
        ----------
        username: str
            Grid username
        key: str
            Grid API key

        Returns
        -------
        """

        #  We'll setup a new credentials header for this request
        #  and also instantiate the client.
        self.__set_authentication_headers(username=username, key=key)
        self._init_client()

        #  Let's create a directory first, using the parent
        #  path to that directory.
        P = Path.home().joinpath(self.grid_credentials_path)
        Path(P.parents[0]).mkdir(parents=True, exist_ok=True)

        query = """
            query Login ($cliVersion: String!) {
                cliLogin (cliVersion: $cliVersion) {
                    userId
                    success
                    message
                }
            }
        """

        #  Get user ID and store in credentials file.
        result = self.query(query, cliVersion=__version__)
        if not result['cliLogin']['success']:
            raise click.ClickException(f"Cannot login: {result['cliLogin']['message']}")

        credentials = {'UserID': result['cliLogin']['userId'], 'APIKey': key}

        #  Writes JSON credentials file.
        with P.open('w') as file:
            json.dump(credentials, file, ensure_ascii=False, indent=4)

    def train(
        self, config: dict, kind: WorkflowType, run_name: str, run_description: str, entrypoint: str,
        script_args: List[str], invocation_command: str
    ) -> None:
        """
        Submits a Run to backend from a local script.

        Parameters
        ----------
        config: dict
            YAML config
        kind: WorkflowType
            Run kind; either SCRIPT or BLUEPRINT. BLUEPRINT not
            supported at the moment,
        run_name: str
            Run name
        run_description: str
            Run description.
        entrypoint: str
            Entrypoint script.
        script_args: List[str]
            Script arguments passed from command line.
        """
        # Check user Github token for user.
        self._check_user_github_token()

        # Check if the active directory is a github.com repository.
        self._check_github_repository()

        # Check if repository contains uncommitted files.
        self._check_if_uncommited_files()

        # Check if remote is in sync with local.
        self._check_if_remote_head_is_different()

        # Checking dependencies and suggesting when needed
        self._check_dependency_listing()

        if kind == WorkflowType.BLUEPRINT:
            raise TrainError('Blueprint workflows are currently not supported.')

        #  Base64-encode the config object either passed
        #  or constructed.
        config_encoded = base64.b64encode(yaml.dump(config).encode('ascii')).decode('ascii')
        env.logger.debug(config_encoded)

        #  Get commit SHA
        commit_sha = execute_git_command(['rev-parse', 'HEAD'])
        env.logger.debug(commit_sha)

        #  Get repo name
        github_repository = execute_git_command(["config", "--get", "remote.origin.url"])
        env.logger.debug(github_repository)

        #  Clean up the repo name
        github_repository = github_repository.replace('git@github.com:', 'github.com/')
        github_repository = github_repository.replace('.git', '')

        if not self._check_github_repo_accessible(github_repository):
            settings_url = env.GRID_URL.replace("graphql", "") + "#/settings?tabId=integrations"
            click.launch(settings_url)
            raise click.ClickException(
                f'Grid cannot access {github_repository}. Please grant access on the settings page: {settings_url}'
            )

        #  Build GraphQL query
        mutation = gql(
            """
        mutation (
            $configString: String!
            $name: String!
            $description: String
            $commitSha: String
            $githubRepository: ID!
            $commandLineArgs: [String]!
            $invocationCommand: String!
            ) {
            trainScript (
                properties: {
                        githubRepository: $githubRepository
                        name: $name
                        description: $description
                        configString: $configString
                        commitSha: $commitSha
                        commandLineArgs: $commandLineArgs
                        invocationCommand: $invocationCommand
                    }
            ) {
            success
            message
            name
            runId
            }
        }
        """
        )

        #  Add the root path to the entrypoint script.
        _entrypoint = Grid._add_git_root_path(entrypoint)

        #  Prepend the file name to the list of args and
        #  builds the query payload.
        script_args.insert(0, _entrypoint)
        params = {
            'configString': config_encoded,
            'name': run_name,
            'description': run_description,
            'commitSha': commit_sha,
            'githubRepository': github_repository,
            'commandLineArgs': script_args,
            'invocationCommand': invocation_command
        }

        #  Send request to Grid.
        try:
            result = self.client.execute(mutation, variable_values=params)
            if env.DEBUG:
                click.echo('Train response')
                click.echo(result)

            message = f"""
                Run submitted!
                `grid status` to list all runs
                `grid status {run_name}` to see all experiments for this run

                ----------------------
                Submission summary
                ----------------------
                script:                  {entrypoint}
                instance_type:           {config['compute']['train']['instance']}
                use_spot:                {config['compute']['train'].get('use_spot', False)}
                cloud_provider:          {config['compute']['provider']['vendor']}
                cloud_credentials:       {config['compute']['provider']['credentials']}
                grid_name:               {run_name}
                datastore_name:          {config['compute']['train'].get('datastore_name')}
                datastore_version:       {config['compute']['train'].get('datastore_version')}
                datastore_mount_dir:     {config['compute']['train'].get('datastore_mount_dir')}
                """
            click.echo(message)

        #  Raise any other errors that the backend may raise.
        except Exception as e:  # skipcq: PYL-W0703
            message = ast.literal_eval(str(e))['message']
            if CREDIT_CARD_ERROR_MESSAGE in message and click.confirm(
                f"{message}\nWould you like to validate one now?"
            ):
                settings_url = env.GRID_URL.replace("graphql", "") + "#/settings?tabId=profile"
                click.launch(settings_url)
            else:
                raise click.ClickException(message)

    # skipcq: PYL-W0102
    def status(
        self,
        kind: Optional[ObservableType] = None,
        identifiers: List[str] = None,
        follow: bool = False,
        export: str = None
    ) -> None:
        """
        The status of an observable object in Grid. That can be a Cluster,
        a Run, or an Experiment.

        Parameters
        ----------
        kind: Optional[ObservableType], default None
            Kind of object that we should get the status from
        identifiers: List[str], default []
            Observable identifiers
        follow: bool, default False
            If we should generate a live table with results.
        export: Optional[str], default None
            What type of file results should be exported to, if any.
        """
        #  We'll instantiate a websocket client when users
        #  want to follow an observable.
        if follow:
            self._init_client(websocket=True)

        kind = kind or ObservableType.RUN

        if kind == ObservableType.EXPERIMENT:
            observable = self.available_observables[kind](client=self.client, identifier=identifiers[0])

        elif kind == ObservableType.RUN:
            if not identifiers:
                observable = self.available_observables[ObservableType.RUN](client=self.client)
            else:
                #  For now, we only check the first observable.
                #  We should also check for others in the future.
                observable = self.available_observables[kind](client=self.client, identifier=identifiers[0])

        elif kind == ObservableType.INTERACTIVE:
            # Create observable.
            observable = self.available_observables[kind](client=self.client)

        elif kind == ObservableType.CLUSTER:
            raise click.BadArgumentUsage("It isn't yet possible to observe clusters.")

        else:
            raise click.BadArgumentUsage('No observable instance created.')

        if follow:
            result = observable.follow()
        else:
            result = observable.get()

        #  Save status results to a file, if the user has specified.
        if export:
            try:

                #  No need to continue if there are not results.
                if not result:
                    click.echo('\nNo run data to write to CSV file.\n')
                    return result

                #  The user may have requested a table of
                #  Runs or Experiments, use the key that is returned
                #  by the API.
                results_key = list(result.keys())[0]

                #  Initialize variables.
                path = None
                now = datetime.now()
                date_string = f'{now:%Y-%m-%d_%H:%M}'

                if export == 'csv':
                    path = f'grid-status-{date_string}.csv'
                    with open(path, 'w') as csv_file:

                        #  We'll exclude any List or Dict from being
                        #  exported in the CSV. We do this to avoid
                        #  generating a CSV that contains JSON data.
                        #  There aren't too many negative sides to this
                        #  because the nested data isn't as relevant.
                        sample = result[results_key][0]
                        _sample = sample.copy()
                        for k, v in _sample.items():
                            if isinstance(v, (list, dict)):
                                del sample[k]  # skipcq: PTC-W0043

                        columns = sample.keys()
                        writer = csv.DictWriter(csv_file, fieldnames=columns)
                        writer.writeheader()
                        for data in result[results_key]:
                            writer.writerow({k: v for k, v in data.items() if k in columns})

                elif export == 'json':
                    path = f'grid_status-{date_string}.json'
                    with open(path, 'w') as json_file:
                        json_file.write(json.dumps(result[results_key]))

                if path:
                    click.echo(f'\nExported status to file: {path}\n')

            #  Catch possible errors when trying to create file
            #  in file system.
            except (IOError, TypeError) as e:
                if env.DEBUG:
                    click.echo(e)

                raise click.FileError('Failed to save grid status to file\n')

        return result

    # skipcq: PYL-W0102
    def history(self, identifiers: List[str] = [], kind: Optional[ObservableType] = ObservableType.RUN) -> None:
        """
        Fetches the history of an observable object in Grid. That can be a
        Cluster, a Run, or an Experiment.

        Parameters
        ----------
        kind: Optional[ObservableType], default ObservableType.RUN
            The kind of object to fetch history from
        identifiers: List[str], default []
            Object identifier, e.g. Experiment ID
        """
        if not kind:
            observable = self.available_observables[ObservableType.RUN]()

        elif kind == ObservableType.EXPERIMENT:
            observable = self.available_observables[kind](client=self.client, identifier=identifiers[0])

        elif kind == ObservableType.RUN:
            if not identifiers:
                observable = self.available_observables[ObservableType.RUN](client=self.client)
            else:
                observable = self.available_observables[kind](client=self.client, identifier=identifiers[0])

        elif kind == ObservableType.CLUSTER:
            raise click.BadArgumentUsage("It isn't yet possible to observe clusters.")

        else:
            raise click.BadArgumentUsage(f"history not supported for kind {kind}")

        return observable.get_history()

    def cancel(self, run_name: Optional[str] = None, experiment_name: Optional[str] = None) -> bool:
        """
        Cancels a run or an experiment.

        Parameters
        ----------
        run_name: Optional[str]
            Run name
        experiment_name: Optional[str]
            Experiment name

        Returns
        -------
        success: bool
            Truthy if operation is successful.
        """
        spinner = None
        try:
            if experiment_name:
                experiment_id = self.get_experiment_id(experiment_name=experiment_name)

                spinner = yaspin.yaspin(text=f'Cancelling experiment {experiment_name}...', color="yellow")
                spinner.start()

                result = self.client.execute(
                    gql(
                        """
                    mutation ($experimentId: ID!) {
                            cancelExperiment(experimentId: $experimentId) {
                                success
                                message
                            }
                        }
                    """
                    ),
                    variable_values={'experimentId': experiment_id}
                )

                if not result['cancelExperiment']['success']:
                    raise click.ClickException(f"{result['cancelExperiment']['message']}")

                spinner.ok("✔")
                styled_name = click.style(experiment_name, fg='blue')
                click.echo(f'Experiment {styled_name} was cancelled successfully.')
            else:
                spinner = yaspin.yaspin(text=f'Cancelling run {run_name}...', color="yellow")
                spinner.start()

                result = self.client.execute(
                    gql(
                        """
                    mutation ($name: ID!) {
                        cancelRun(name: $name) {
                            success
                            message
                        }
                    }
                    """
                    ),
                    variable_values={'name': run_name}
                )

                if not result['cancelRun']['success']:
                    raise click.ClickException(f"{result['cancelRun']['message']}")

                spinner.ok("✔")
                styled_name = click.style(run_name, fg='blue')
                click.echo(f'Run {styled_name} was cancelled successfully.')
        except Exception as e:
            if spinner:
                spinner.fail("✘")
            raise click.ClickException(f"Cancel failed: {e}")
        finally:
            if spinner:
                spinner.stop()

        return True

    def create_interactive_node(self, config: dict, name: str, description: str) -> bool:
        """
        Creates an interactive node via Grid.

        Parameters
        ----------
        config: dict
            YAML config
        name: str
            Name of interactive node to use
        description: str
            Description of interactive node

        Returns
        -------
        success: bool
            Truthy if operation is successful.
        """
        spinner = yaspin.yaspin(text="Creating Interactive node ...", color="yellow")
        spinner.start()

        config_yaml = yaml.dump(config)

        #  Base64-encode the config object either passed
        #  or constructed.
        config_encoded = base64.b64encode(config_yaml.encode('ascii')).decode('ascii')

        #  Cancel the entire Run otherwise.
        mutation = gql(
            """
        mutation (
            $name: ID!
            $description: String
            $configString: String!
        ) {
            createInteractiveNode(properties: {
                                    name: $name, description: $description,
                                    configString: $configString
                                  }) {
                success
                message
            }
        }
        """
        )

        params = {
            'name': name,
            'description': description,
            'configString': config_encoded,
        }
        try:
            result = self.client.execute(mutation, variable_values=params)

            message = f"""
                Interactive node created!

                `grid status` to list all runs and interactive nodes.
                `grid status {name}` to see the status for this interactive node.

                ----------------------
                Submission summary
                ----------------------
                name:                    {name}
                instance_type:           {config['compute']['train']['instance']}
                cloud_provider:          {config['compute']['provider']['vendor']}
                cloud_credentials:       {config['compute']['provider']['credentials']}
                datastore_name:          {config["compute"]["train"].get("datastore_name")}
                datastore_version:       {config["compute"]["train"].get("datastore_version")}
                datastore_mount_dir:     {config["compute"]["train"].get("datastore_mount_dir")}
                """

            click.echo(message)
        except Exception as e:  # skipcq: PYL-W0703
            message = ast.literal_eval(str(e))['message']
            spinner.fail("✘")
            raise click.ClickException(message)

        success = result['createInteractiveNode']['success']
        if success:
            spinner.ok("✔")
            click.echo(f'Interactive node {name} is spinning up.')

        elif not success:
            spinner.fail("✘")
            message = result['createInteractiveNode']['message']
            #click.echo(message)
            if CREDIT_CARD_ERROR_MESSAGE in message and click.confirm(
                f"{message}\nWould you like to validate one now?"
            ):
                settings_url = env.GRID_URL.replace("graphql", "") + "#/settings?tabId=profile"
                click.launch(settings_url)
            else:
                raise click.ClickException(message)

        return success

    def pause_interactive_node(self, interactive_node_name: str) -> None:
        """
        Pauses an interactive node.

        Parameters
        ----------
        interactive_node_name: str
            Interactive node ID
        """
        spinner = yaspin.yaspin(text="Pausing Interactive node ...", color="yellow")
        spinner.start()

        mutation = gql(
            """
        mutation (
            $interactiveNodeName: ID!
        ) {
            pauseInteractiveNode(interactiveNodeName: $interactiveNodeName) {
                success
                message
            }
        }
        """
        )

        params = {'interactiveNodeName': interactive_node_name}

        success = False
        try:
            result = self.client.execute(mutation, variable_values=params)
        except Exception as e:  # skipcq: PYL-W0703
            message = ast.literal_eval(str(e))['message']
            spinner.fail("✘")
            raise click.ClickException(message)

        success = result['pauseInteractiveNode']['success']
        if success:
            spinner.ok("✔")
            click.echo(f'Interactive node {interactive_node_name} has ' + 'been paused successfully.')

        elif not success:
            spinner.fail("✘")
            if env.DEBUG:
                click.echo(f"→ {result['pauseInteractiveNode']['message']}")

            raise click.ClickException(f"Failed to pause interactive node '{interactive_node_name}'")

        return success

    def resume_interactive_node(self, interactive_node_name: str) -> None:
        """
        Resumes an interactive node.

        Parameters
        ----------
        interactive_node_name: str
            Interactive node ID
        """
        spinner = yaspin.yaspin(text="Resuming Interactive node ...", color="yellow")
        spinner.start()

        mutation = gql(
            """
        mutation (
            $interactiveNodeName: ID!
        ) {
            resumeInteractiveNode(interactiveNodeName: $interactiveNodeName) {
                success
                message
            }
        }
        """
        )

        params = {'interactiveNodeName': interactive_node_name}

        success = False
        try:
            result = self.client.execute(mutation, variable_values=params)
        except Exception as e:  # skipcq: PYL-W0703
            message = ast.literal_eval(str(e))['message']
            spinner.fail("✘")
            raise click.ClickException(message)

        success = result['resumeInteractiveNode']['success']
        if success:
            spinner.ok("✔")
            click.echo(f'Interactive node {interactive_node_name} has ' + 'been resumed successfully.')

        elif not success:
            spinner.fail("✘")
            if env.DEBUG:
                click.echo(f"→ {result['resumeInteractiveNode']['message']}")

            raise click.ClickException(f"Failed to resume interactive node '{interactive_node_name}'")

        return success

    def delete_interactive_node(self, interactive_node_name: str) -> None:
        """
        Deletes an interactive node from cluster.

        Parameters
        ----------
        interactive_node_name: str
            Interactive node ID
        """
        spinner = yaspin.yaspin(text="Deleting Interactive node ...", color="yellow")
        spinner.start()

        mutation = gql(
            """
        mutation (
            $interactiveNodeName: ID!
        ) {
            deleteInteractiveNode(interactiveNodeName: $interactiveNodeName) {
                success
                message
            }
        }
        """
        )

        params = {'interactiveNodeName': interactive_node_name}

        success = False
        try:
            result = self.client.execute(mutation, variable_values=params)
        except Exception as e:  # skipcq: PYL-W0703
            message = ast.literal_eval(str(e))['message']
            spinner.fail("✘")
            raise click.ClickException(message)

        success = result['deleteInteractiveNode']['success']
        if success:
            spinner.ok("✔")
            click.echo(f'Interactive node {interactive_node_name} has ' + 'been deleted successfully.')

        elif not success:
            spinner.fail("✘")
            if env.DEBUG:
                click.echo(f"→ {result['deleteInteractiveNode']['message']}")

            raise click.ClickException(f"Failed to delete interactive node '{interactive_node_name}'")

        return success

    def get_experiment_id(self, experiment_name: str) -> str:
        """
        Get experiment ID from name.

        Parameters
        ----------
        experiment_name: str
            Experiment name

        Returrns
        --------
        experiment_id: str
            Experiment ID
        """
        try:
            spinner = yaspin.yaspin(text="Getting experiment info...", color="yellow")
            spinner.start()

            result = self.client.execute(
                gql(
                    """
                    query ($experimentName: String!) {
                        getExperimentId(experimentName: $experimentName) {
                            success
                            message
                            experimentId
                        }
                    }
                    """
                ),
                variable_values={'experimentName': experiment_name}
            )

            if not result['getExperimentId']['success']:
                raise click.ClickException(f"{result['getExperimentId']['message']}")

            spinner.ok("✔")
        except Exception as e:
            spinner.fail("✘")
            raise click.ClickException(f"Could not find experiment: {e}")
        finally:
            spinner.stop()

        return result['getExperimentId']['experimentId']

    def experiment_details(self, experiment_id: str) -> Dict[str, Any]:
        """
        Get experiment details.

        Parameters
        ----------
        experiment_id: str
            Experiment ID

        Returrns
        --------
        details: Dict[str, Any]
            Experiment details
        """
        # If job is queued, notify the user that logs aren't available yet
        query = gql(
            """
        query (
            $experimentId: ID!
        ) {
            getExperimentDetails(experimentId: $experimentId) {
                experimentId
                run {
                  name
                }
                status
            }
        }
        """
        )
        params = {'experimentId': experiment_id}
        result = self.client.execute(query, variable_values=params)

        return result

    # TODO: refactor this to break into smaller methods.
    def experiment_logs(
        self,
        experiment_name: str,
        n_lines: int = 50,
        page: Optional[int] = None,
        max_lines: Optional[int] = None,
        use_pager: bool = False
    ) -> Dict[str, str]:
        """
        Gets experiment logs from a single experiment.

        Parameters
        ----------
        n_lines: int, default 200
            Max number of lines to return
        experiment_name: str
            Experiment name for a single experiment
        page: Optional[int], default None
            Which page of logs to fetch.
        max_lines: Optional[int], default None
            Maximum number of lines to print in terminal.
        use_pager: bool, default False
            If the log results should be a scrollable pager.
        """
        experiment_id = self.get_experiment_id(experiment_name=experiment_name)

        #  Starts spinner.
        spinner = yaspin.yaspin(text="Fetching logs ...", color="yellow")
        spinner.start()

        # If the experiment is in a finished state, then
        # get logs from archive.
        finished_states = ('failed', 'succeeded', 'cancelled')
        experiment_details = self.experiment_details(experiment_id=experiment_id)

        # Check if Experiment is queued.
        state = experiment_details['getExperimentDetails']['status']

        if state == 'queued':
            spinner.ok("✔")
            styled_queued = click.style('queued', fg='yellow')
            click.echo(
                f"""
                Your Experiment is {styled_queued}. Logs will be available
                when your Experiment starts.
                        """
            )
            spinner.stop()
            return

        # Check if the user has requested logs from the
        # archive explicitly or if the experiment is in a
        # finished state.
        is_archive_request = page is not None
        is_finished_state = state in finished_states
        if is_archive_request or is_finished_state:

            query = gql(
                """
            query GetLogs ($experimentId: ID!, $page: Int) {
                getArchiveExperimentLogs(experimentId: $experimentId, page: $page) {
                    lines {
                        message
                        timestamp
                    }
                    currentPage
                    totalPages
                }
            }
            """
            )
            params = {'experimentId': experiment_id, 'page': page}
            try:
                result = self.client.execute(query, variable_values=params)

            #  Raise any other errors that the backend may raise.
            except Exception as e:  # skipcq: PYL-W0703
                spinner.fail("✘")
                if 'Server error:' in str(e):
                    e = str(e).replace('Server error: ', '')[1:-1]

                message = ast.literal_eval(str(e))['message']
                raise click.ClickException(message)

            # The backend will return end empty object if no pages
            # of logs are available.
            if not result.get('getArchiveExperimentLogs') or not result['getArchiveExperimentLogs'].get('lines'):
                spinner.stop()
                raise click.ClickException(f'No logs available for experiment {experiment_name}')

            # Print message to help users read all logs.
            separator = '-' * 80
            page_command_message = f"""We will be displaying logs from the archives.

        $ grid logs {experiment_name}
    {separator}"""

            # Print messages indicating that other log pages are
            # available.
            styled_experiment_name = click.style(experiment_name, fg='blue')
            styled_state = click.style(state, fg='magenta')
            prompt_message = f"""

    The Experiment {styled_experiment_name} is in a finished
    state ({styled_state}). {page_command_message}

            """

            if is_archive_request:
                prompt_message = page_command_message

            spinner.ok("✔")
            spinner.stop()
            click.echo(prompt_message)

            # Get all log lines.
            lines = result['getArchiveExperimentLogs']['lines']
            total_lines = len(lines)
            if total_lines > self.acceptable_lines_to_print and not max_lines:
                styled_total_lines = click.style(str(total_lines), fg='red')
                too_many_lines_message = f"""    {click.style('NOTICE', fg='yellow')}: The log stream you requested contains {styled_total_lines} lines.
    You can limit how many lines to print by using:

        $ grid logs {experiment_name} --max_lines 50


    Would you like to proceed? """
                click.confirm(too_many_lines_message, abort=True, default=True)

            # Style the log lines.
            styled_logs = []
            for log in lines[:max_lines]:

                # If no timestamps are returned, fill the field
                # with dashes.
                if not log['timestamp']:
                    # Timestamps have 32 characters.
                    timestamp = click.style('-' * 32, fg='green')
                else:
                    timestamp = click.style(log['timestamp'], fg='green')

                styled_logs.append(f"[{timestamp}] {log['message']}")

            # Either print the logs in the terminal or use the pager
            # to scroll through the logs.
            if use_pager:
                click.echo_via_pager(styled_logs)
            else:
                for line in styled_logs:
                    click.echo(line, nl=False)

        # If the experiment isn't in a finished state, then
        # do a subscription with live logs.
        else:

            #  Let's first change the client transport to use
            #  a websocket transport instead of using the regular
            #  HTTP transport.
            self._init_client(websocket=True)

            subscription = gql(
                """
            subscription GetLogs ($experimentId: ID!, $nLines: Int!) {
                getLiveExperimentLogs(
                    experimentId: $experimentId, nLines: $nLines) {
                        message
                        timestamp
                }
            }
            """
            )

            params = {'experimentId': experiment_details['getExperimentDetails']['experimentId'], 'nLines': n_lines}

            # Create websocket connection.
            connection_closed_message = "Connection closed. Please try again."
            try:
                stream = self.client.subscribe(subscription, variable_values=params)

                first_run = True
                for log in stream:

                    #  Closes the spinner.
                    if first_run:
                        spinner.ok("✔")
                        first_run = False

                    #  Prints each line to terminal.
                    log_entries = log['getLiveExperimentLogs']
                    for entry in log_entries:
                        # If no timestamps are returned, fill the field
                        # with dashes.
                        if not entry['timestamp']:
                            # Timestamps have 32 characters.
                            timestamp = click.style('-' * 32, fg='green')
                        else:
                            timestamp = click.style(entry['timestamp'], fg='green')

                        click.echo(f"[{timestamp}] {entry['message']}", nl=False)

            # If connection is suddenly closed, indicate that a
            # known error happened.
            except websockets.exceptions.ConnectionClosed:
                spinner.fail("✘")
                raise click.ClickException(connection_closed_message)

            except websockets.exceptions.ConnectionClosedOK:
                spinner.fail("✘")
                raise click.ClickException('Could not continue fetching log stream.')

            # Raise any other errors that the backend may raise.
            except Exception as e:  # skipcq: PYL-W0703
                raise click.ClickException(connection_closed_message)

        #  Makes sure to close the spinner in all situations.
        #  If we don't do this, the tracker character in the terminal
        #  disappears.
        spinner.stop()

    def experiment_metrics(self, experiment_name: str, metric: str, n_lines: int = 50) -> Dict[str, str]:
        """
        Gets experiment scalar logs from a single experiment.

        Parameters
        ----------
        experiment_name: str
            Experiment name for a single experiment
        metric: str
            Metric names
        n_lines: int, default 50
            Max number of lines to return
        """
        experiment_id = self.get_experiment_id(experiment_name=experiment_name)

        #  Starts spinner.
        spinner = yaspin.yaspin(text="Fetching metrics ...", color="yellow")
        spinner.start()

        experiment_details = self.experiment_details(experiment_id=experiment_id)

        # Check if Experiment is queued.
        state = experiment_details['getExperimentDetails']['status']
        if state == 'queued':
            spinner.ok("✔")
            styled_queued = click.style('queued', fg='yellow')
            click.echo(
                f"""
    Your Experiment is {styled_queued}. Metrics will be available
    when your Experiment starts.
            """
            )
            spinner.stop()
            return

        query = gql(
            """
        query GetScalarLogs ($experimentId: ID!, $metric: String!, $startIndex: Int, $format: String) {
            getExperimentScalarLogs(experimentId: $experimentId,
                                    metric: $metric,
                                    startIndex: $startIndex,
                                    format: $format) {
                values
                steps
                nextIndex
            }
        }
        """
        )

        params = {'experimentId': experiment_id, 'metric': metric, 'startIndex': 0, 'format': 'json'}

        try:
            result = self.client.execute(query, variable_values=params)
        #  Raise any other errors that the backend may raise.
        except Exception as e:  # skipcq: PYL-W0703
            spinner.fail("✘")
            if 'Server error:' in str(e):
                e = str(e).replace('Server error: ', '')[1:-1]

            message = ast.literal_eval(str(e))['message']
            raise click.ClickException(message)

        metric = result['getExperimentScalarLogs']
        # The backend will return an empty object if no metrics
        # are available.
        if not metric or not metric['steps']:
            spinner.stop()
            raise click.ClickException(f'No metrics available for experiment {experiment_id}')

        spinner.ok("✔")
        spinner.stop()

        # TODO: Change when encoding and compression is fixed in
        # backend API
        # def decode(x: bytes, dtype: str):
        #     buf = zlib.decompress(base64.b64decode(x.encode()))
        #     out = array(dtype)
        #     out.frombytes(buf)
        #     return out

        try:
            # steps = decode(metric['steps'], 'q')
            # values = decode(metric['values'], 'd')

            steps = json.loads(metric['steps'])
            values = json.loads(metric['values'])
        #  Raise any other errors that the backend may raise.
        except Exception as e:
            spinner.fail("✘")
            if 'Server error:' in str(e):
                e = str(e).replace('Server error: ', '')[1:-1]

            message = ast.literal_eval(str(e))['message']
            raise click.ClickException(message)

        if n_lines > 0:
            steps = steps[-n_lines:]
            values = values[-n_lines:]

        # Get all metrics in lines
        lines = [f"{step:>16}  {value:.10f}\n" for step, value in zip(steps, values)]

        # Print the metrics in the terminal
        for line in lines:
            click.echo(line, nl=False)

        #  Makes sure to close the spinner in all situations.
        #  If we don't do this, the tracker character in the terminal
        #  disappears.
        spinner.stop()

    def delete(self, experiment_name: Optional[str] = None, run_name: Optional[str] = None) -> bool:
        """
        Deletes an experiment or a run

        Parameters
        ----------
        experiment_name : Optional[str]
            experiment name of experiment to be deleted
        run_name : Optional[str]
            run name of run to be deleted

        Returns
        -------
        success: bool
            Truthy if operation is successful
        """
        spinner = None
        try:
            if experiment_name:
                experiment_id = self.get_experiment_id(experiment_name=experiment_name)

                spinner = yaspin.yaspin(text=f'Deleting experiment {experiment_name}...', color="yellow")
                spinner.start()

                result = self.client.execute(
                    gql(
                        """
                    mutation ($experimentId: ID!) {
                        deleteExperiment(experimentId: $experimentId) {
                            success
                            message
                        }
                    }"""
                    ),
                    variable_values={'experimentId': experiment_id}
                )

                if not result['deleteExperiment']['success']:
                    raise click.ClickException(f"{result['deleteExperiment']['message']}")

                spinner.ok("✔")
                styled_name = click.style(experiment_name, fg='blue')
                click.echo(f'Experiment {styled_name} was deleted successfully.')
            else:
                spinner = yaspin.yaspin(text=f'Deleting run {run_name}...', color="yellow")
                spinner.start()

                result = self.client.execute(
                    gql(
                        """
                    mutation ($name: ID!) {
                        deleteRun(name: $name) {
                            success
                            message
                        }
                    }"""
                    ),
                    variable_values={'name': run_name}
                )

                if not result['deleteRun']['success']:
                    raise click.ClickException(f"{result['deleteRun']['message']}")

                spinner.ok("✔")
                styled_name = click.style(run_name, fg='blue')
                click.echo(f'Run {styled_name} was deleted successfully.')
        except Exception as e:
            if spinner:
                spinner.fail("✘")
            raise click.ClickException(f"Delete failed: {e}")
        finally:
            if spinner:
                spinner.stop()

        return True

    def delete_datastore(self, name: str, version: int, credential_id: str):
        """
        Delete datastore for user

        Parameters
        ----------
        name: str
            Datastore name
        version: int
            Datastore version
        credential_id: str
            Credential Id
        """
        mutation = gql(
            """
            mutation (
                $name: String!
                $version: Int!
                $credentialId: String!
                ) {
                deleteDatastore (
                    properties: {
                            name: $name,
                            version: $version,
                            credentialId: $credentialId
                        }
                ) {
                success
                message
                }
            }
            """
        )

        params = {'name': name, 'version': version, 'credentialId': credential_id}

        spinner = yaspin.yaspin(text=f'Deleting datastore {name} with version {version}', color="yellow")
        spinner.start()

        try:
            result = self.client.execute(mutation, variable_values=params)
            success = result['deleteDatastore']['success']
            message = result['deleteDatastore']['message']

            if success:
                spinner.text = "Finished deleting datastore."
                spinner.ok("✔")
            else:
                spinner.text = f'Failed to delete datastore {name} with version ' \
                               f'{version}: {message}'
                spinner.fail("✘")

        except Exception as e:  #skipcq: PYL-W0703
            spinner.fail("✘")
            raise click.ClickException(f'Failed to delete datastore {name} with version {version}. {e}')

        spinner.stop()
        return success

    def resume_datastore_session(self, session_name: str):
        """
        Resume uploading a datastore session

        Parameters
        ----------
        session_name: str
            Name of session
        """
        sessions = DatastoreUploadSession.recover_sessions()
        session = None
        for s in sessions:
            if s.session_name == session_name:
                session = s
                break

        if not session:
            self.__print_datastore_sessions(sessions)
            raise click.ClickException(
                f"No session named {session_name} found, please specify an " + "available session"
            )

        session.configure(client=self.client)
        try:
            session.upload()
        except Exception as e:  #skipcq: PYL-W0703
            import traceback
            traceback.print_exc()
            raise click.ClickException(f'Failed to upload datastore {session.name}. {e}')

    @staticmethod
    def __print_datastore_sessions(sessions: List[DatastoreUploadSession]):
        """
        Print the table of datastore sessions
        """
        click.echo("Available datastore incomplete uploads that can be resumed: ")
        table_cols = ['Name', 'Version', "Command to resume"]
        table = BaseObservable.create_table(columns=table_cols)
        for session in sessions:
            command = f"grid datastore resume {session.session_name}"
            table.add_row(session.name, str(session.version), command)

        console = Console()
        console.print(table)

    def list_resumable_datastore_sessions(self):
        """
        List datastores that can be resumed upload
        """
        sessions = DatastoreUploadSession.recover_sessions()
        if len(sessions) == 0:
            return

        click.echo("")
        click.echo("")
        self.__print_datastore_sessions(sessions)

    def validate_datastore_version(self, grid_config: dict):
        """
        Find maximum version of a datastore (ready to attach) and set config accordingly.
        No-op if config does not contain datastore name or already contains a set datastore version.
        """
        try:
            datastore_name = grid_config["compute"]["train"]["datastore_name"]
            datastore_version = grid_config["compute"]["train"]["datastore_version"]
        except:
            return

        if datastore_version or not datastore_name:
            return

        query = gql(
            """
            query GetDatastores {
                getDatastores {
                    name
                    version
                    snapshotStatus
                }
            }
        """
        )

        try:
            result = self.client.execute(query)
        except TransportQueryError as e:
            raise click.ClickException(f"Unable to list datastores: {e}")

        max_version = -1
        for row in result["getDatastores"]:
            if datastore_name == row["name"] and row['snapshotStatus'] == "succeeded":
                max_version = max(max_version, int(row["version"]))

        if max_version == -1:
            raise click.ClickException(
                f'No --grid_datastore_version passed for datastore: {datastore_name}, but unable to find a ready-to-use version.'
            )

        click.echo(f'No --grid_datastore_version passed for datastore: {datastore_name}. Using version: {max_version}')
        grid_config["compute"]["train"]["datastore_version"] = str(max_version)

    def list_datastores(self):
        """
        List datastores for user
        """
        query = gql(
            """
            query GetDatastores {
                getDatastores {
                    id
                    credentialId
                    name
                    version
                    size
                    createdAt
                    snapshotStatus
                }
            }
        """
        )
        try:
            result = self.client.execute(query)
        except TransportQueryError as e:
            raise click.ClickException(f"Unable to list datastores: {e}")

        table_cols = ["Credential Id", "Name", "Version", "Size", "Created", "Status"]
        table = BaseObservable.create_table(columns=table_cols)
        sorted_datastores = sorted(result["getDatastores"], key=lambda k: (k['name'], k['version']))
        for row in sorted_datastores:
            created_at = date_string_parse(row["createdAt"])
            created_at = f'{created_at:%Y-%m-%d %H:%M}'
            size = row["size"]
            if size or size == 0:
                size = humanize.naturalsize(size * (1024**2))

            if row['snapshotStatus'] in {'pending', 'preparing', 'queued', 'running'}:
                status = 'Optimizing'
            else:
                status = row['snapshotStatus'].title() if row['snapshotStatus'] else "Unknown"

            table.add_row(row["credentialId"], row["name"], row["version"], size, created_at, status)

        console = Console()
        console.print(table)

    def upload_datastore(self, source: str, name: str, credential_id: str, compression: bool):
        """
        Uploads datastore to storage

        Parameters
        ----------
        source: str
           Source to create datastore from, either a local directory or a
           http url.
        name: str
           Name of datastore
        credential_id: str
            Grid credential id
        compression: str
            Enable compression, which is disabled by default

        Returns
        -------
        success: bool
            Truthy when a datastore has been uploaded
            correctly.
        """
        try:
            session = create_datastore_session(
                name=name, source=source, credential_id=credential_id, compression=compression, client=self.client
            )
            session.upload()
        except Exception as e:  #skipcq: PYL-W0703
            raise click.ClickException(f'Failed to upload datastore {name}. {e}')

        return True

    def add_ssh_public_key(self, key: str, name: str):
        return self.query(
            """
            mutation (
                $publicKey: String!
                $name: String!
            ) {
            addSSHPublicKey(name: $name, publicKey: $publicKey) {
                message
                success
                id
              }
            }
        """,
            publicKey=key,
            name=name
        )

    def list_public_ssh_keys(self, limit: int) -> List[Dict[str, str]]:
        result = self.query(
            """
            query (
                $limit: Int!,
            ) {
                getPublicSSHKeys(limit: $limit) {
                    id
                    publicKey,
                    name
              }
            }
        """,
            limit=limit,
        )
        return result['getPublicSSHKeys']

    def delete_ssh_public_key(self, key_id: str):
        self.query(
            """
            mutation (
                $id: ID!
            ) {
              deleteSSHPublicKey(id: $id) {
                message
                success
              }
            }
        """,
            id=key_id
        )

    def list_interactive_node_ssh_setting(self):
        return self.query(
            """
        query {
            getInteractiveNodes {
                name: interactiveNodeName
                ssh_url: sshUrl
                status
            }
        }
        """
        )['getInteractiveNodes']

    @staticmethod
    def _gen_ssh_config(
        interactive_nodes: List[Dict[str, Any]],
        curr_config: str,
        start_marker: str = "### grid.ai managed BEGIN do not edit manually###",
        end_marker: str = "### grid.ai managed END do not edit manually###",
    ):

        content = curr_config.splitlines()
        sol = []
        managed_part = [start_marker]
        for node in interactive_nodes:
            if node["status"] != "running":
                continue

            ssh_url = urlsplit(node['ssh_url'])
            managed_part.extend([
                f"Host {node['name']}",
                f"    User {ssh_url.username}",
                f"    Hostname {ssh_url.hostname}",
                f"    Port {ssh_url.port}",
                "    StrictHostKeyChecking accept-new",
                "    CheckHostIP no",
            ])
        managed_part.append(end_marker)

        within_section = False
        added_managed_part = False
        for line in content:
            if line == start_marker:
                if added_managed_part:
                    raise ValueError("Found 2 start markers")
                if within_section:
                    raise ValueError("Found 2 start markers in row")
                within_section = True
            elif end_marker == line:
                if added_managed_part:
                    raise ValueError("Found 2+ start end")
                if not within_section:
                    raise ValueError("End marker before start marker")
                within_section = False
                sol.extend(managed_part)
                added_managed_part = True
            elif not within_section:
                sol.append(line)
        if within_section:
            raise ValueError("Found only start marker, no end one found")
        if not added_managed_part:
            sol.extend(managed_part)
        return '\n'.join(sol)

    def sync_ssh_config(self) -> List[str]:
        """
        sync local ssh config with grid's interactive nodes config

        Returns
        -------
        list of interactive nodes present
        """
        interactive_nodes = self.list_interactive_node_ssh_setting()

        ssh_config = Path(env.GRID_SSH_CONFIG)
        if not ssh_config.exists():
            ssh_config.write_text("")

        ssh_config.write_text(
            self._gen_ssh_config(
                interactive_nodes=interactive_nodes,
                curr_config=ssh_config.read_text(),
            )
        )

        return interactive_nodes

    def check_is_blocked(self) -> None:
        """Checks if user account is currently blocked from performing operations on Grid."""
        query = """
        query {
            getUser {
                isVerified
                completedSignup
                isBlocked
            }
        }
        """
        data = self.query(query)["getUser"]
        if data.get("isVerified") is False:
            raise click.UsageError(
                f"User account not yet verified. Verify your account at {env.GRID_URL}/#/verification"
            )

        if data.get("completedSignup") is False:
            raise click.UsageError(
                f"You haven't yet completed registration. Please complete registration at {env.GRID_URL}/#/registration"
            )

        if data.get("isBlocked") is True:
            raise click.UsageError("Your account is blocked. Please reach out to support at support@grid.ai")

    def is_run(self, run_name: str):
        """Checks if a resource is a run."""
        query = gql(
            """
            query (
                $runName: ID
            ) {
                getRuns (runName: $runName) {
                    name
                }
            }
        """
        )

        try:
            self.client.execute(query, variable_values={'runName': run_name})
            return True
        except Exception as e:
            if 'No active runs' in str(e):
                return False
            raise e

    def is_interactive_node(self, interactive_node_name: str):
        """Checks if a resource is an interactive node."""
        query = gql(
            """
            query GetInteractiveNodes{
                getInteractiveNodes {
                    interactiveNodeName
                }
            }
        """
        )

        result = self.client.execute(query)
        nodes = {i['interactiveNodeName'] for i in result['getInteractiveNodes']}

        return interactive_node_name in nodes

    def get_user_info(self):
        """Return basic information about a user."""
        query = gql(
            """
            query {
                getUser {
                    username
                    firstName
                    lastName
                    email

                }
            }
        """
        )

        return self.client.execute(query)['getUser']
