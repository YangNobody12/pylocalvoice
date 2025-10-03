# Contributing to pyhmong

Thank you for your interest in contributing to pyhmong! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background, identity, or experience level.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them get started
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

### Unacceptable Behavior

- Harassment, discrimination, or intimidation
- Trolling, insulting, or derogatory comments
- Personal or political attacks
- Publishing others' private information
- Other conduct that could reasonably be considered inappropriate

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:

```bash
git clone https://github.com/YOUR_USERNAME/pyhmong.git
cd pyhmong
```

3. Add the upstream repository:

```bash
git remote add upstream https://github.com/yangnobody12/pyhmong.git
```

## Development Setup

### Install Development Dependencies

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Or use make
make install-dev
```

### Verify Installation

```bash
# Run tests
pytest

# Check code quality
make lint
```

## How to Contribute

### Reporting Bugs

Before creating a bug report:
- Check if the bug has already been reported in the Issues section
- Verify the bug exists in the latest version

When creating a bug report, include:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Python version and operating system
- Code samples if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:
- Use a clear, descriptive title
- Provide a detailed description of the proposed enhancement
- Explain why this enhancement would be useful
- List any alternative solutions you've considered

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:
- `good first issue` - Simple issues for beginners
- `help wanted` - Issues where we need community help

### Development Workflow

1. Create a new branch:

```bash
git checkout -b feature/amazing-feature
```

2. Make your changes
3. Add tests for your changes
4. Run the test suite:

```bash
make test
```

5. Format your code:

```bash
make format
```

6. Commit your changes:

```bash
git add .
git commit -m "Add amazing feature"
```

7. Push to your fork:

```bash
git push origin feature/amazing-feature
```

8. Open a Pull Request

## Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:
- Maximum line length: 100 characters
- Use 4 spaces for indentation (no tabs)
- Use meaningful variable names
- Add docstrings to all public methods and classes

### Code Formatting

We use **Black** for code formatting:

```bash
black pyhmong tests
```

### Import Ordering

We use **isort** for import ordering:

```bash
isort pyhmong tests
```

### Type Hints

Add type hints to all function signatures:

```python
def tokenize(text: str) -> List[str]:
    """Tokenize Hmong text."""
    pass
```

### Docstring Format

Use Google-style docstrings:

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of function.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When value is invalid
        
    Example:
        >>> example_function("test", 42)
        True
    """
    pass
```

## Testing Guidelines

### Writing Tests

- Write tests for all new features
- Maintain or improve code coverage
- Use descriptive test names
- Group related tests in classes

### Test Structure

```python
class TestFeatureName(unittest.TestCase):
    """Test cases for FeatureName."""
    
    def setUp(self):
        """Set up test fixtures."""
        pass
    
    def test_basic_functionality(self):
        """Test basic functionality works."""
        pass
    
    def test_edge_cases(self):
        """Test edge cases are handled."""
        pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_pyhmong.py

# Run specific test
pytest tests/test_pyhmong.py::TestHmongProcessor::test_tokenize

# Run with coverage
make coverage
```

### Test Coverage

- Aim for at least 80% code coverage
- Critical code paths should have 100% coverage
- Check coverage report:

```bash
make coverage
open htmlcov/index.html
```

## Documentation

### Code Documentation

- Add docstrings to all public classes and methods
- Include examples in docstrings when helpful
- Update documentation when changing functionality

### README Updates

If your change affects:
- Installation process
- API usage
- Features list
- Examples

Please update the README.md accordingly.

### Building Documentation

```bash
# Build HTML documentation
make docs

# View documentation
open docs/_build/html/index.html
```

## Pull Request Process

### Before Submitting

1. Update tests
2. Update documentation
3. Run the full test suite
4. Format your code
5. Update CHANGELOG.md (if applicable)

### PR Description

Include in your PR description:
- What changes were made
- Why these changes were necessary
- How to test the changes
- Screenshots (if UI changes)
- Related issue numbers

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts with main branch

### Review Process

1. Automated checks will run (tests, linting)
2. Maintainers will review your code
3. Address any requested changes
4. Once approved, a maintainer will merge

### After Merge

1. Delete your feature branch
2. Update your local main branch:

```bash
git checkout main
git pull upstream main
```

## Project Structure

```
pyhmong/
├── pyhmong/           # Main package
│   ├── __init__.py    # Package initialization
│   ├── core.py        # Core functionality
│   └── data/          # Data files
├── tests/             # Test suite
│   └── test_pyhmong.py
├── docs/              # Documentation
├── examples.py        # Usage examples
├── setup.py           # Package setup
└── README.md          # Project readme
```

## Communication

### Asking Questions

- GitHub Discussions for general questions
- GitHub Issues for bug reports and feature requests
- Email for security vulnerabilities

### Keeping Updated

- Watch the repository for notifications
- Check the CHANGELOG for updates
- Follow project announcements

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

If you have questions about contributing, feel free to:
- Open a discussion on GitHub
- Reach out to maintainers
- Ask in existing issues

Thank you for contributing to pyhmong! 🎉