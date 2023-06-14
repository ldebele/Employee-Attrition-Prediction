from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()
    requirements = [lib.replace('\n', '') for lib in requirements]


setup(
    name="Employee_Attrition_Prediction",
    version="1.0",
    description="",
    author="Lemi Debele",
    author_email="lemidebele@gmail.com",
    packages=find_packages(),

    install_requires=requirements,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

)