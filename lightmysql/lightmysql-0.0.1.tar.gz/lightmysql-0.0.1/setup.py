from setuptools import setup, find_packages

setup(
    name='lightmysql',
    version='0.0.1',
    description='The improved-package of pymysql.',
    py_modules=["lightmysqls"],


    long_description="The improved-package of pymysql, made by Yixiangzhilv.",
    url='https://github.com/Danny-Yxzl/',
    author='Yixiangzhilv',
    author_email='mail@yixiangzhilv.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='sql mysql pymysql database',
    install_requires=['pymysql'],
    project_urls={
        'Bug Reports': 'https://github.com/Danny-Yxzl/',
        'Say Thanks!': 'https://www.yixiangzhilv.com/',
        'Source': 'https://github.com/Danny-Yxzl/',
    })
