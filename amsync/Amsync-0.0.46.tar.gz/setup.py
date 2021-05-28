from setuptools import setup, find_packages


with open('README.md', 'r') as stream:
    long_description = stream.read()

setup(
    name='Amsync',
    version='0.0.46',
    url='https://github.com/ellandor/Amsync',
    license='MIT',
    author='SempreLegit',
    description='An async library to easily create bots for the amino.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        'aminoapps',
        'amino-py',
        'amino',
        'amino-bot',
        'narvii',
        'api',
        'python',
        'python3',
        'python3.x',
        'amino-async',
    ],
    install_requires=[
        'aiohttp',
        'ujson',
        'pybase64',
        'peewee',
        'python-dotenv',
        'pillow',
        'colorama',
        'python-magic-bin'
    ],
    setup_requires=['wheel'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    entry_points={
        'console_scripts': [
            'amsync = scripts.amsync:main',
        ]
    },
    packages=find_packages(),
)
