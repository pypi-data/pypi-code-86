from setuptools import find_packages, setup


setup(
    name="dnastack-client-library",
    packages=find_packages(exclude=["dnastack.cli"]),
    version="0.0.11",
    description="DNAstack CLI Library",
    author="Derek, Joseph, Usanthan",
    hiddenimports=["cmath"],
    license="MIT",
    install_requires=[
        "search-python-client>=0.1.9",
        "urllib3==1.26.3",
        "requests==2.25.1",
        "click==7.1.2",
        "altgraph==0.17",
        "macholib==1.14",
        "pyyaml==5.4.1",
    ],
    entry_points={"console_scripts": ["dnastack = dnastack.__main__:dnastack"]},
)
