from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A package example'

with open("README.md","r") as fh:
    long_description = fh.read()

# Setting up
setup(
        name="ExamplePackage3",
        version=VERSION,
        author="An Phan",
        author_email = "<ahphan@iastate.edu>",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[],
        py_modules=["hello"],
        package_dir={'': 'src'},
        url="https://github.com/anphan0828/ExamplePackage3.git",
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
        ]
)
