from setuptools import setup,find_packages
from typing import List


#declairng variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Prachi Gupta"
DESCRIPTION="This is first project"
PAKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    pakages=find_packages(),#search a folder that contain __init__.py file,return all pakages name 
    install_requires=get_requirements_list()
)

