from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()
    requirements = [r.replace('\n', '') for r in requirements]


# creating a setup file for the project.
setup(
    name="Employee_Attrition_Prediction",
    version="1.0",
    author="Lemi Debele",
    author_email="lemidebele@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
)