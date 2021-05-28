#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests'
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest', 'flake8', 'vcrpy'
]

setup(
    name='zammad_py',
    version='1.0.0',
    description="Python API client for zammad",
    long_description=readme + '\n\n' + history,
    author="Joe Paul",
    author_email='joeirimpan@gmail.com',
    url='https://github.com/joeirimpan/zammad_py',
    packages=find_packages(include=['zammad_py']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='zammad_py',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
