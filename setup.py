"""
Setup script for pyhmong package
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    """Read a file and return its contents."""
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, filename), encoding='utf-8') as f:
        return f.read()

# Read version from __init__.py
def get_version():
    """Extract version from package."""
    with open('pyhmong/__init__.py', 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split("'")[1]
    return '0.1.0'

setup(
    name='pyhmong',
    version=get_version(),
    description='A professional Python library for Hmong language processing',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/pyhmong',
    license='MIT',
    
    # Package configuration
    packages=find_packages(exclude=['tests', 'docs']),
    python_requires='>=3.7',
    
    # Dependencies
    install_requires=[
        # Add any required packages here
    ],
    
    # Optional dependencies for development
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'black>=22.0.0',
            'flake8>=5.0.0',
            'mypy>=0.990',
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
        'test': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
    },
    
    # Classifiers help users find your project
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Hmong',
    ],
    
    # Keywords for PyPI
    keywords='hmong language nlp linguistics text-processing',
    
    # Entry points for command-line scripts (if needed)
    entry_points={
        'console_scripts': [
            # 'pyhmong=pyhmong.cli:main',  # Uncomment if you add CLI
        ],
    },
    
    # Include additional files
    include_package_data=True,
    package_data={
        'pyhmong': ['data/*.txt', 'data/*.json'],  # Include data files if any
    },
    
    # Project URLs
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/pyhmong/issues',
        'Source': 'https://github.com/yourusername/pyhmong',
        'Documentation': 'https://pyhmong.readthedocs.io',
    },
)