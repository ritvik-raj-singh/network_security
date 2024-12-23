'''
The setup.py file is an essential part of packagin and distributing Python 
Projects. It is used by setuptools to deifne the configuration
 of your project, such as its metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

requirement_lst:List[str]=[]

def get_requirements()->List[str]:
    """
    This function will return list of requirments
    """

    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines= file.readlines()
            for line in lines:
                requirement=line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1",
    author="Ritvik Raj",
    author_email="ritvikraj.ipl@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)