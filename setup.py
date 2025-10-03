#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for PyHmong
=========================

Installation:
    pip install .
    pip install -e .  # Development mode
    pip install -e ".[dev]"  # With dev dependencies

Build:
    python setup.py sdist bdist_wheel

Upload to PyPI:
    twine upload dist/*
"""

import os
import sys
from setuptools import setup, find_packages

# Read version from __init__.py
def get_version():
    """Extract version from package __init__.py"""
    init_path = os.path.join(
        os.path.dirname(__file__), 
        'pyhmong', 
        '__init__.py'
    )
    
    if os.path.exists(init_path):
        with open(init_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('__version__'):
                    # Extract version string
                    return line.split("'")[1]
    return '0.1.0'

# Read long description from README
def read_file(filename):
    """Read a file and return its contents."""
    here = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(here, filename)
    
    if os.path.exists(file_path):
        with open(file_path, encoding='utf-8') as f:
            return f.read()
    return ''

# Get version
VERSION = get_version()

# Long description from README
LONG_DESCRIPTION = read_file('README.md')
if not LONG_DESCRIPTION:
    LONG_DESCRIPTION = """
PyHmong - A Professional Python Library for Hmong Language Processing
=====================================================================

A comprehensive Python library offering 7 major feature categories:

1. Phonology & Orthography - Text normalization, tone analysis
2. Dictionary & Translation - Hmong ↔ English translation
3. Grammar - POS tagging, classifiers, conjugation
4. Phrasebook Utilities - Common phrases and dialogues
5. Numbers & Measures - Number conversion and measurements
6. Proverbs & Idioms - Cultural expressions
7. Education Tools - Pronunciation drills and flashcards

Features:
- 22+ functions across 7 categories
- 100+ word dictionary
- Zero external dependencies
- Full RPA romanization support
- Professional code structure

Visit: https://github.com/yangnobody12/pyhmong
"""

# Setup configuration
setup(
    # Basic information
    name='pyhmong',
    version=VERSION,
    description='A professional Python library for Hmong language processing',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    
    # Author information
    author='YangNobody12',
    author_email='yangnobody12@example.com',
    maintainer='YangNobody12',
    maintainer_email='yangnobody12@example.com',
    
    # Project URLs
    url='https://github.com/yangnobody12/pyhmong',
    project_urls={
        'Bug Reports': 'https://github.com/yangnobody12/pyhmong/issues',
        'Source': 'https://github.com/yangnobody12/pyhmong',
        'Documentation': 'https://github.com/yangnobody12/pyhmong#readme',
        'Changelog': 'https://github.com/yangnobody12/pyhmong/blob/main/CHANGELOG.md',
    },
    
    # License
    license='MIT',
    
    # Package configuration
    packages=find_packages(exclude=['tests', 'tests.*', 'docs', 'examples']),
    package_data={
        'pyhmong': [
            'data/*.txt',
            'data/*.json',
            'data/*.csv',
        ],
    },
    include_package_data=True,
    
    # Python version requirement
    python_requires='>=3.7',
    
    # Dependencies
    install_requires=[
        # No external dependencies! Uses only Python standard library
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            # Testing
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'pytest-xdist>=3.0.0',
            'coverage>=7.0.0',
            
            # Code quality
            'black>=22.0.0',
            'flake8>=5.0.0',
            'mypy>=0.990',
            'pylint>=2.15.0',
            'isort>=5.10.0',
            
            # Documentation
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
            'sphinx-autodoc-typehints>=1.19.0',
            
            # Development tools
            'ipython>=8.0.0',
            'jupyter>=1.0.0',
            
            # Build and distribution
            'build>=0.9.0',
            'twine>=4.0.0',
            'wheel>=0.38.0',
        ],
        'test': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
        ],
        'docs': [
            'sphinx>=5.0.0',
            'sphinx-rtd-theme>=1.0.0',
        ],
    },
    
    # PyPI classifiers
    classifiers=[
        # Development status
        'Development Status :: 3 - Alpha',
        
        # Intended audience
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        
        # License
        'License :: OSI Approved :: MIT License',
        
        # Programming language
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        
        # Topics
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        
        # Natural language
        'Natural Language :: Hmong',
        'Natural Language :: English',
        
        # Operating systems
        'Operating System :: OS Independent',
        
        # Other
        'Typing :: Typed',
    ],
    
    # Keywords for PyPI
    keywords=[
        'hmong',
        'language',
        'nlp',
        'natural-language-processing',
        'linguistics',
        'text-processing',
        'translation',
        'dictionary',
        'grammar',
        'education',
        'rpa',
        'romanization',
        'tones',
        'phonology',
    ],
    
    # Entry points (if you want CLI commands)
    entry_points={
        'console_scripts': [
            # Uncomment to add command-line interface
            # 'pyhmong=pyhmong.cli:main',
        ],
    },
    
    # Zip safe (for egg distributions)
    zip_safe=False,
    
    # Platform
    platforms='any',
)

# Post-installation message (without emoji for Windows compatibility)
if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("PyHmong Installation Complete!")
    print("=" * 70)
    print("\nQuick Start:")
    print("  >>> import pyhmong")
    print("  >>> pyhmong.normalize_text('kuv yog neeg')")
    print("  >>> pyhmong.translate_hm_to_en('niam')")
    print("\nDocumentation: https://github.com/yangnobody12/pyhmong")
    print("Issues: https://github.com/yangnobody12/pyhmong/issues")
    print("\nThank you for using PyHmong! Ua tsaug!")
    print("=" * 70 + "\n")