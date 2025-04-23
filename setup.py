"""
The setup.py file is an essential part of packaging and distributing python projects. 
It is used by setuptools (or distutils in older Python version) to define the configuration
of your project, such as its metadata, dependencies and more...
"""

from setuptools import find_packages, setup  # scan all the folders with a __init__.py file that are considered as packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    try:
        with open("requirements.txt", "r") as file:

            # read lines from the file
            lines = file.readlines()

            ## process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found")
    
    return requirement_list

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Stefano Dalle Carbonare",
    author_email="stefanodallecarbonare99@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements() # install all the libraries
)

