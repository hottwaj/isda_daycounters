import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "isda_daycounters",
    version = "0.0.1",
    author = "MitchellEdwardSnaith",
    author_email = "",
    description = ("ISDA day-count conventions with year-fractions and day-counts"),
    license = "?",
    keywords = "isda daycount convention",
    url = "https://github.com/MitchellEdwardSnaith/isda_daycounters",
    packages=['isda_daycounters', 'isda_daycounters.tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Finance",
        "License :: ?",
    ],
)
