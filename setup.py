from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'A package example'

# Setting up
setup(
        name="ExamplePackage2",
        version=VERSION,
        author="An Phan",
        author_email = "<ahphan@iastate.edu>",
        description=DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
        ]
)
