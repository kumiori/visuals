# setup.py
from setuptools import setup, find_packages

setup(
    name='visuals',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        # add other dependencies if needed
    ],
    author='Andrés A León Baldelli',
    author_email='leon.baldelli@cnrs.fr',
    description='Default plotting settings and utilities.',
    url='https://github.com/yourusername/visuals',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)