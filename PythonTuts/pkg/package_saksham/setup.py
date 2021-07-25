from setuptools import setup, find_packages, version

setup(name="package_saksham", 
version= "0.3",# Maine version change kar diya pehle 0.1 
 description = "This is a code with harry package",
long_description= "This is a very very long description",
author = "Saksham", 
 packages = ['package_saksham'],
 install_requires= []# If we have imported any module in __init__.py , we have to write it in the list
)
