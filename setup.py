import os

from setuptools import setup, find_packages

def readme() -> str:
    """Utility function to read the README.md.

    Used for the `long_description`. It's nice, because now
    1) we have a top level README file and
    2) it's easier to type in the README file than to put a raw string in below.

    Args:
        nothing

    Returns:
        String of readed README.md file.
    """
    return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='happiness_index',
    version='0.1.0',
    author='Alejandro Delgado Tech',
    author_email='alejandrodelgado_2000@hotmail.com',
    description='This project show how from the pre proccessing to the modeling of a dataset in order to have important features',
    python_requires='>=3',
    license='',
    url='',
    packages=find_packages(),
    long_description=readme(),
)