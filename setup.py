from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the `requirements.txt` file and returns a list of dependencies.

    Returns:
        List[str]: A list of package requirements.
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and `-e .`
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Error: requirements.txt file not found")
    return requirement_list

setup(
    name = 'NetworkSecurity',
    version="0.0.1",
    author="Sumanth",
    author_email="ssumanth510@gmail.com",
    packages=find_packages(),
    install_requirements = get_requirements()
    )