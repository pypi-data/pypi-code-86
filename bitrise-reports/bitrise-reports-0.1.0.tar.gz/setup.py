# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bitrise_reports']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.1',
 'openpyxl==3.0.7',
 'pretty-errors==1.2.21',
 'python-dateutil==2.8.1',
 'requests==2.25.1',
 'rich==10.2.2']

entry_points = \
{'console_scripts': ['bitrise-reports = bitrise_reports:main']}

setup_kwargs = {
    'name': 'bitrise-reports',
    'version': '0.1.0',
    'description': 'The missing tool to extract reports about projects you build on Bitrise',
    'long_description': '# Bitrise Reports\n\n[![Flake8](https://img.shields.io/badge/codestyle-flake8-yellow)](https://flake8.pycqa.org/en/latest/)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Quality](https://api.codeclimate.com/v1/badges/a9fe25bd995710be45d2/maintainability)](https://codeclimate.com/github/dotanuki-labs/bitrise-reports/maintainability)\n[![Coverage](https://codecov.io/gh/dotanuki-labs/bitrise-reports/branch/main/graph/badge.svg)](https://codecov.io/gh/dotanuki-labs/bitrise-reports)\n[![PyPI](https://img.shields.io/pypi/v/bitrise-reports)](https://pypi.org/project/bitrise-reports/)\n[![Main](https://github.com/dotanuki-labs/bitrise-reports/workflows/Main/badge.svg)](https://github.com/dotanuki-labs/bitrise-reports/actions?query=workflow%3AMain)\n[![License](https://img.shields.io/github/license/dotanuki-labs/bitrise-reports)](https://choosealicense.com/licenses/mit)\n\n## What\n\nA simple cruncher for numbers derived from builds you run on [Bitrise CI](https://www.bitrise.io/). Useful if you are in charge of managing infrastructure capacity related to Bitrise, like detecting/reporting anomalies, evaluating queues impact and so on.\n\nMain features:\n\n- Backed by [Bitrise REST API](https://api-docs.bitrise.io/) under the hood\n- Can compute timing (queued, running and total execution time) for all builds in the given time window\n- Can compute build statuses (success, failure or aborted) for all builds in the given time window\n- Results can be filtered by Git branch (eg **master** or **main**)\n- Result are detailed per machine type and also per Workflow\n- Supports emulation of consumed [Bitrise Velocity credits](https://www.bitrise.io/velocity-plan) (for Enterprise customers)\n- Report types : CLI (stdout), JSON and Excel spreadsheet\n\n## Installing\n\nThis tool requires Python, supporting versions 3.8.x and 3.9.x.\n\nInstall `bitrise-reports` with [pip](https://pypi.org/project/pip/)\n\n```bash\n→ pip install bitrise-reports\n```\n\n## Using\n\nLet\'s say you want analyse numbers for the project `android-flagship`, learning from\nbuilds that ran during April of 2021. You\'ll firstly need a\n[Bitrise Personal Access Token](https://devcenter.bitrise.io/api/authentication/) for\nthat. Note you must be a member in the project you want to analyse.\n\nBy running\n\n```bash\n→ bitrise-reports \\\n    --token=$BITRISE_PAT_TOKEN \\\n    --app=my-app \\\n    --starting=2021-04-01 \\\n    --ending=2021-04-30\n```\nyou should get something like that on your CLI\n\n![](.github/assets/showcase-cli-simple.png)\n\nwhich is a simple overview of what happened.\n\nLet\'s say now that you want to learn about how much time you are spending with queued builds.\n\nYou can run then\n\n```bash\n→ bitrise-reports \\\n    --token=$BITRISE_PAT_TOKEN \\\n    --app=my-app \\\n    --starting=2021-04-01 \\\n    --ending=2021-04-30 \\\n    --detailed-timing\n```\n\nand get a report like this one\n\n![](.github/assets/showcase-cli-timing.png)\n\nLast but not least, suppose you want to learn about execution status for all your Workflows that you run for events in your `master` branch (eg, push or a scheduled build).\n\nYou can run\n\n```bash\n→ bitrise-reports \\\n    --token=$BITRISE_PAT_TOKEN \\\n    --app=my-app \\\n    --starting=2021-04-01 \\\n    --ending=2021-04-30 \\\n    --target-branch=master \\\n    --detailed-builds\n```  \n\nand get a report like about that too\n\n![](.github/assets/showcase-cli-statuses.png)\n\n## Command line interface\n\nThe complete list of CLI options:\n\n| Option           | Details                                                         | Required  |\n|------------------|-----------------------------------------------------------------|-----------|\n| token            | Personal access token for Bitrise API                           | Yes       |\n| app              | The title of your app in Bitrise                                | Yes       |\n| starting         | Starting date in the target time frame                          | Yes       |\n| ending           | Ending date in the target time frame                            | Yes       |\n| detailed-builds  | Details all statuses (success, failure and abortion) for builds | No        |\n| detailed-timing  | Details timing (queued, running, total execution) for builds    | No        |\n| emulate-velocity | Estimate Bitrise Velocity credits consumed                      | No        |\n| target-branch    | Filters build by Git branch                                     | No        |\n| report-style     | The style of report you want                                    | No        |\n\nwhere\n\n- `starting` and `ending` follow **YYYY-MM-DD** convention\n- `report-style` accepts **stdout** (default), **json** or **excel**\n- `detailed-timing` is a CLI flag\n- `detailed-builds` is a CLI flag\n- `emulate-velocity` is a CLI flag\n\nIf you opt-in for a specific report style, the corresponding file - **bitrise-metrics.json** or **bitrise-metrics.xlsx** - will be written in the same folder you are runnint `bitrise-reports`.\n\n## Contributing\n\nIf you want to contribute with this project\n\n- Check the [contribution guidelines](https://github.com/dotanuki-labs/.github/blob/main/CONTRIBUTING.md)\n- Ensure you have Python 3.8.+ installed. I recommend [Pyenv](https://github.com/pyenv/pyenv) for that.\n- Ensure you have [Poetry](https://python-poetry.org/) installed\n- Prepare your environment with [Flake8](https://pypi.org/project/flake8/), [Black](https://pypi.org/project/black/) and [Bandit](https://pypi.org/project/bandit/)\n\n```bash\n→ make setup\n```\n\n- Code you changes\n- Make sure you have a green build\n\n```bash\n→  make inspect test\n```\n\n- Submit your PR 🔥\n\n## Author\n\n- Coded by Ubiratan Soares (follow me on [Twitter](https://twitter.com/ubiratanfsoares))\n\n## License\n\n```\nThe MIT License (MIT)\n\nCopyright (c) 2021 Dotanuki Labs\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of\nthis software and associated documentation files (the "Software"), to deal in\nthe Software without restriction, including without limitation the rights to\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\nthe Software, and to permit persons to whom the Software is furnished to do so,\nsubject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n```\n',
    'author': 'Ubiratan Soares',
    'author_email': 'ubiratanfsoares@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dotanuki-labs/bitrise-reports',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
