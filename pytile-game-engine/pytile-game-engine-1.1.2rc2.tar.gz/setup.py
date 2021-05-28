import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pytile-game-engine",
    version="1.1.2rc2",
    description="A simple library for tilemaps in python/pygame.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/enbyte/pytile",
    author="Enbyte Games",
    author_email="sb-mangobrains@crowder-sklar.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["src/pytile"],
    include_package_data=True,
    install_requires=["pygame", "numpy", "tkinter"],
)
