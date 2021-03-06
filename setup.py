import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pydl",
    version = "0.3.6",
    author = "Samuel Thomas",
    author_email = "sgpthomas@gmail.com",
    description = ("A python library designed to make analyzing timeseries data easy."),
    packages=['pydl', 'pydl.io', 'pydl.draw', 'pydl._analysis'],
    long_description=read('README.md'),
)
