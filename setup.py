from setuptools import setup, find_packages
setup(
    name="clc",
    version="0.1",
    description='A useful module',
    packages=find_packages(),
    test_suite="tests",
    scripts=[
        'calculator_app.py',
        'README.md',]
)