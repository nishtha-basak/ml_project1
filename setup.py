from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path:str) -> List[str]:

    """
    Reads a requirements file and returns a list of dependencies.
    
    Args:
        file_path (str): Path to the requirements file.
        
    Returns:
        list: A list of dependencies.
    """
    requirments=[]
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments= [req.replace("\n"," ") for req in requirments]

# we do not want to include -e . in our requirements.txt file
    # if '-e .' is present in the requirements, we remove it
        if '-e .' in requirments:
         requirments.remove('-e .')
         return requirments


setup(
    name='mlproject1',  # Replace with your package name 
    version='0.0.1',  # Replace with your package version 
    author='Nishtha Basak',  # Replace with your name  
    author_email='nishthabasak@gmail.com',  # Replace with your email
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=get_requirements('requirements.txt'),  # Install dependencies from requirements.txt
)