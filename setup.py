import os
import setuptools
import configparser

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

try:
    version = os.environ["TRAVIS_TAG"]
except KeyError:
    version = "v0.0.0"

config = configparser.ConfigParser()
pip_file = config.read("Pipfile")
packages = [package for package in config["packages"]]

setuptools.setup(
    name="madplot",
    version=version,
    install_requires=packages,
    entry_points={
        'console_scripts': [
            'madplot=madplot:main',
        ],
    },
    author="naka345",
    author_email="nakaka33@yahoo.co.jp",
    description="package test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naka345/madplot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    python_requires='>=3.8',
)
