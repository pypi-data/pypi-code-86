#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['pymultirole_plugins']

package_data = \
{'': ['*']}

install_requires = \
['pydantic==1.7.3', 'fastapi==0.61.2', 'pytest']

setup(name='pymultirole-plugins',
      version='0.2.55',
      description='Sherpa multirole plugins',
      author='Olivier Terrier',
      author_email='olivier.terrier@kairntech.com',
      url='https://kairntech.com/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      python_requires='>=3.8',
     )
