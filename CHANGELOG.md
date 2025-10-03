# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Pahawh Hmong script support
- Extended dictionary with 1000+ words
- Dialect support (White Hmong, Green Hmong)
- Text-to-speech integration
- Language detection
- CLI tool for text processing
- Web API wrapper

## [0.1.0] - 2025-10-03

### Added
- Initial release of pyhmong
- Core `HmongProcessor` class for text processing
- `HmongDictionary` class with basic vocabulary
- Support for Romanized Popular Alphabet (RPA) system
- Text tokenization functionality
- Syllable validation
- Tone marker extraction and analysis
- Syllable decomposition (onset, nucleus, coda)
- Text normalization
- Comprehensive test suite with 80%+ coverage
- Complete documentation and examples
- MIT License
- Professional project structure

### Features
- Tokenize Hmong text into syllables
- Validate Hmong syllables
- Extract tone markers from syllables
- Decompose syllables into components
- Count syllables in text
- Normalize text formatting
- Dictionary lookup for common words
- Support for single consonants, digraphs, and trigraphs
- Support for simple and complex vowels
- All 7 tone markers plus unmarked tone

### Developer Tools
- Unit tests with pytest
- Code coverage reporting
- Code formatting with Black
- Linting with flake8
- Type checking with mypy
- Makefile for common tasks
- Development dependencies configuration

### Documentation
- Comprehensive README with examples
- API reference documentation
- Contributing guidelines
- Code of conduct
- Usage examples file
- Inline code documentation

## Version History Details

### [0.1.0] - 2025-10-03

This is the first public release of pyhmong. The library provides essential tools for working with Hmong text in Python.

**Core Components:**

1. **HmongProcessor**
   - Main text processing engine
   - Implements RPA romanization system
   - Provides tokenization, validation, and analysis

2. **HmongDictionary**
   - Basic dictionary with ~20 common words
   - Extensible design for adding new words
   - Case-insensitive lookup

3. **Enums**
   - `RomanizationSystem`: RPA and PAHAWH (placeholder)
   - `ToneMarker`: All 8 Hmong tones

**Technical Details:**

- Written in pure Python (3.7+)
- No external dependencies for core functionality
- Type hints throughout
- Comprehensive docstrings
- 80%+ test coverage
- Follows PEP 8 style guide

**Known Limitations:**

- Only RPA romanization currently implemented
- Limited dictionary size
- No dialect-specific features
- No audio/pronunciation support
- No machine learning features

**Future Improvements:**

See the [Unreleased] section above for planned features.

## Release Notes Format

Each release follows this format:

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security fixes

---

## How to Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to pyhmong.

## Support

- **Issues**: [GitHub Issues](https://github.com/yangnobody12/pyhmong/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yangnobody12/pyhmong/discussions)

[Unreleased]: https://github.com/yangnobody12/pyhmong/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/yangnobody12/pyhmong/releases/tag/v0.1.0