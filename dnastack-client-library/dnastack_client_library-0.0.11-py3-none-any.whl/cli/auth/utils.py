import click
import datetime as dt
from dnastack.cli.utils import has_config, get_config
from dnastack.cli.auth.commands import cli_login


def get_oauth_token(ctx):

    if not has_config(ctx, "oauth_token"):
        return
    refresh_token(ctx)
    return get_config(ctx, "oauth_token")


def refresh_token(ctx):

    # there is no good way got telling if the server is authenticated yet,
    # so if the user does not have a token set up, assume that is is public and
    # don't do anything
    ctx.invoke(cli_login, refresh=True)
