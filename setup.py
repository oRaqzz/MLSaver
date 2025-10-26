from setuptools import setup, find_packages

setup(
    name="MLSaver", 
    version="0.2",  
    author="raad",
    description="A simple ML model versioning tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "joblib>=1.5.2",
    ]
)