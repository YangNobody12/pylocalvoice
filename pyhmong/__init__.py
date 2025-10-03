"""
pyhmong - A professional Python library for Hmong language processing
======================================================================

This package provides comprehensive tools for working with the Hmong language,
including text processing, linguistic analysis, and dictionary support.

Basic usage:
    >>> import pyhmong
    >>> text = "Kuv yog neeg Hmoob"
    >>> tokens = pyhmong.tokenize(text)
    >>> print(tokens)
    ['Kuv', 'yog', 'neeg', 'Hmoob']

For more advanced usage, see the documentation at:
https://pyhmong.readthedocs.io
"""

__version__ = '0.1.0'
__author__ = 'YangNobody12'
__email__ = 'yangnobody12@example.com'
__license__ = 'MIT'

from .core import (
    HmongProcessor,
    HmongDictionary,
    RomanizationSystem,
    ToneMarker,
    tokenize,
    is_valid_syllable,
    normalize,
)

__all__ = [
    # Version info
    '__version__',
    '__author__',
    '__email__',
    '__license__',
    
    # Classes
    'HmongProcessor',
    'HmongDictionary',
    'RomanizationSystem',
    'ToneMarker',
    
    # Convenience functions
    'tokenize',
    'is_valid_syllable',
    'normalize',
]

# Module level docstring for help()
def _get_module_info():
    """Return module information."""
    return {
        'version': __version__,
        'author': __author__,
        'license': __license__,
    }


if __name__ == '__main__':
    # Display package info when run directly
    print(f"pyhmong version {__version__}")
    print(f"Author: {__author__}")
    print(f"License: {__license__}")
    print("\nFor usage examples, see: https://github.com/yangnobody12/pyhmong")