from setuptools import find_packages, setup
from typing import List
'''
so this will automatically find out all the packages that are available in the in the entire uh in the entire machine learning 
application in the directory that we have actually created
'''

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of reuirements
    '''
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        # print(requirements)
        requirements=[req.replace("\n","") for req in requirements]

    # print(requirements)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            

    return requirements

# get_requirements('requirements.txt')

#you can basically consider this as a metadata information about the entire project
setup(
    name="mlproject",
    version='0.0.1',
    author='Nikhil',
    author_email='poojarynikhil047@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)