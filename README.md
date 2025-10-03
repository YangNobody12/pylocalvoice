# pyhmong 🇱🇦

[![PyPI version](https://badge.fury.io/py/pyhmong.svg)](https://badge.fury.io/py/pyhmong)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/yourusername/pyhmong/workflows/tests/badge.svg)](https://github.com/yourusername/pyhmong/actions)

A professional Python library for Hmong language processing. This library provides tools for working with the Hmong language, including text processing, romanization systems, and linguistic utilities.

## Features

- **Text Tokenization**: Split Hmong text into syllables
- **Syllable Validation**: Check if syllables are valid Hmong words
- **Tone Analysis**: Extract and analyze Hmong tones
- **Syllable Decomposition**: Break down syllables into onset, nucleus, and coda
- **Text Normalization**: Standardize Hmong text formatting
- **Dictionary Support**: Built-in dictionary with common Hmong words
- **RPA Support**: Full support for Romanized Popular Alphabet system

## Installation

### Enums

**RomanizationSystem:**
- `RPA`: Romanized Popular Alphabet (default)
- `PAHAWH`: Pahawh Hmong script

**ToneMarker:**
- `B`: mid-low tone
- `J`: high falling tone
- `V`: mid-high rising tone
- `S`: low breathy tone
- `G`: low falling tone
- `D`: high tone
- `M`: low glottalized tone
- `NONE`: mid tone (unmarked)

## Project Structure

```
pyhmong/
├── pyhmong/
│   ├── __init__.py          # Package initialization
│   ├── core.py              # Main library code
│   └── data/                # Data files (if any)
├── tests/
│   ├── __init__.py
│   └── test_pyhmong.py      # Unit tests
├── docs/                    # Documentation
├── setup.py                 # Package setup
├── README.md                # This file
├── LICENSE                  # MIT License
├── requirements.txt         # Dependencies
├── requirements-dev.txt     # Development dependencies
├── .gitignore              # Git ignore rules
└── pytest.ini              # Pytest configuration
```

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pyhmong --cov-report=html

# Run specific test file
pytest tests/test_pyhmong.py

# Run specific test
pytest tests/test_pyhmong.py::TestHmongProcessor::test_tokenize_basic
```

### Code Quality

```bash
# Format code with Black
black pyhmong tests

# Lint with flake8
flake8 pyhmong tests

# Type checking with mypy
mypy pyhmong
```

### Building Documentation

```bash
cd docs
make html
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Style Guidelines

- Follow PEP 8 style guide
- Use Black for code formatting
- Write docstrings for all public methods
- Add unit tests for new features
- Update documentation as needed

## Roadmap

- [ ] Support for Pahawh Hmong script
- [ ] Advanced dictionary with more words
- [ ] Text-to-speech integration
- [ ] Language detection
- [ ] Dialect support (White Hmong, Green Hmong)
- [ ] Machine translation support
- [ ] Named entity recognition
- [ ] Part-of-speech tagging

## Resources

### Learn More About Hmong Language

- [Hmong Language Wikipedia](https://en.wikipedia.org/wiki/Hmong_language)
- [RPA Romanization System](https://en.wikipedia.org/wiki/Romanized_Popular_Alphabet)
- [Hmong Dictionary Online](https://hmongdictionary.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Hmong community for preserving this beautiful language
- Inspired by various NLP libraries and linguistic research
- Built with modern Python best practices

## Citation

If you use this library in your research, please cite:

```bibtex
@software{pyhmong,
  author = {YangNobody12},
  title = {pyhmong: A Python Library for Hmong Language Processing},
  year = {2025},
  url = {https://github.com/yangnobody12/pyhmong}
}
```

## Support

- **Issues**: [GitHub Issues](https://github.com/yangnobody12/pyhmong/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yangnobody12/pyhmong/discussions)
- **Email**: yangnobody12@example.com

## Changelog

### Version 0.1.0 (2025-10-03)

- Initial release
- Basic text processing functions
- Syllable validation and decomposition
- Tone marker support
- Simple dictionary implementation
- RPA romanization support

---

Made with ❤️ for the Hmong community From PyPI (when published)

```bash
pip install pyhmong
```

### From Source

```bash
git clone https://github.com/yangnobody12/pyhmong.git
cd pyhmong
pip install -e .
```

### For Development

```bash
git clone https://github.com/yangnobody12/pyhmong.git
cd pyhmong
pip install -e ".[dev]"
```

## Quick Start

```python
import pyhmong

# Tokenize Hmong text
text = "Kuv yog neeg Hmoob"
tokens = pyhmong.tokenize(text)
print(tokens)  # ['Kuv', 'yog', 'neeg', 'Hmoob']

# Check if a syllable is valid
print(pyhmong.is_valid_syllable("kuv"))  # True
print(pyhmong.is_valid_syllable("xyz"))  # False

# Normalize text
normalized = pyhmong.normalize("kuv   yog  neeg")
print(normalized)  # "Kuv yog neeg"
```

## Usage Examples

### Basic Text Processing

```python
from pyhmong import HmongProcessor

processor = HmongProcessor()

# Tokenize text
text = "Nyob zoo, koj nyob li cas?"
tokens = processor.tokenize(text)
print(tokens)

# Count syllables
count = processor.count_syllables(text)
print(f"Number of syllables: {count}")

# Validate syllables
syllables = ["kuv", "koj", "xyz", "peb"]
for syllable in syllables:
    valid = processor.is_valid_syllable(syllable)
    print(f"{syllable}: {valid}")
```

### Tone Analysis

```python
from pyhmong import HmongProcessor

processor = HmongProcessor()

# Get tone of a syllable
tone = processor.get_tone("kuv")
print(f"Tone: {tone}")  # ToneMarker.V: 'mid-high rising tone'

# Decompose syllables
syllable = "ntxawg"
parts = processor.decompose_syllable(syllable)
print(parts)  # {'onset': 'ntx', 'nucleus': 'aw', 'coda': 'g'}
```

### Dictionary Lookup

```python
from pyhmong import HmongDictionary

dictionary = HmongDictionary()

# Look up words
print(dictionary.lookup("kuv"))  # "I, me"
print(dictionary.lookup("koj"))  # "you"

# Add custom words
dictionary.add_word("tsev", "house")
print(dictionary.lookup("tsev"))  # "house"

# Get all words
all_words = dictionary.get_all_words()
print(f"Dictionary has {len(all_words)} words")
```

### Advanced Usage

```python
from pyhmong import HmongProcessor, RomanizationSystem

# Initialize with specific romanization system
processor = HmongProcessor(system=RomanizationSystem.RPA)

# Get linguistic components
consonants = processor.get_initial_consonants()
vowels = processor.get_vowels()

print(f"Number of consonants: {len(consonants)}")
print(f"Number of vowels: {len(vowels)}")

# Process multiple texts
texts = [
    "Kuv yog neeg Hmoob",
    "Koj nyob qhov twg?",
    "Peb mus tsev"
]

for text in texts:
    tokens = processor.tokenize(text)
    normalized = processor.normalize(text)
    print(f"Original: {text}")
    print(f"Tokens: {tokens}")
    print(f"Normalized: {normalized}")
    print()
```

## API Reference

### HmongProcessor

Main class for processing Hmong text.

**Methods:**
- `tokenize(text: str) -> List[str]`: Tokenize text into syllables
- `is_valid_syllable(syllable: str) -> bool`: Check if syllable is valid
- `get_tone(syllable: str) -> Optional[ToneMarker]`: Extract tone from syllable
- `decompose_syllable(syllable: str) -> Dict`: Break down syllable structure
- `count_syllables(text: str) -> int`: Count syllables in text
- `normalize(text: str) -> str`: Normalize text formatting
- `get_initial_consonants() -> Set[str]`: Get all valid consonants
- `get_vowels() -> Set[str]`: Get all valid vowels

### HmongDictionary

Dictionary class for Hmong words.

**Methods:**
- `lookup(word: str) -> Optional[str]`: Look up word definition
- `add_word(word: str, definition: str)`: Add new word to dictionary
- `get_all_words() -> List[str]`: Get all words in dictionary

###