import setuptools 
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ni",
    version="0.1",
    author="digitalphant0m",
    author_email="nswright11@gmail.com",
    description="A python unit testing tool that requires more than just shrubbery",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digitalphant0m/ni",
    packages=find_packages(),
    scripts=['ni.py','__init__.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
