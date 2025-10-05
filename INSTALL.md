# Installation Guide for PyLocalVoice

This guide covers all the ways to install pylocalvoice on your system.

## Table of Contents

- [Requirements](#requirements)
- [Installation Methods](#installation-methods)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Virtual Environments](#virtual-environments)
- [Development Installation](#development-installation)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Upgrading](#upgrading)
- [Uninstallation](#uninstallation)

## Requirements

### System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher
- **Disk Space**: ~5 MB

### Python Packages

pylocalvoice has **no external dependencies** for core functionality! It uses only Python's standard library.

## Installation Methods

### Method 1: Install from PyPI (Recommended)

Once published, install using pip:

```bash
pip install pylocalvoice
```

To install a specific version:

```bash
pip install pylocalvoice==0.1.0
```

### Method 2: Install from Source

#### Using pip

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
pip install .
```

#### For Development

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
pip install -e ".[dev]"
```

### Method 3: Download and Install

1. Download the latest release from [GitHub Releases](https://github.com/yangnobody12/pylocalvoice/releases)
2. Extract the archive
3. Navigate to the directory
4. Install:

```bash
cd pylocalvoice-0.1.0
pip install .
```

### Method 4: Using pipx (Isolated Environment)

```bash
pipx install pylocalvoice
```

## Platform-Specific Instructions

### Windows

#### Using Command Prompt

```cmd
python -m pip install pylocalvoice
```

#### Using PowerShell

```powershell
python -m pip install pylocalvoice
```

#### Using Anaconda

```bash
conda activate your_environment
pip install pylocalvoice
```

### macOS

#### Using Terminal

```bash
pip3 install pylocalvoice
```

#### Using Homebrew Python

```bash
/usr/local/bin/pip3 install pylocalvoice
```

### Linux

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3-pip
pip3 install pylocalvoice
```

#### Fedora/RHEL/CentOS

```bash
sudo dnf install python3-pip
pip3 install pylocalvoice
```

#### Arch Linux

```bash
sudo pacman -S python-pip
pip install pylocalvoice
```

## Virtual Environments

### Using venv (Recommended)

```bash
# Create virtual environment
python -m venv pylocalvoice_env

# Activate on Windows
pylocalvoice_env\Scripts\activate

# Activate on macOS/Linux
source pylocalvoice_env/bin/activate

# Install pylocalvoice
pip install pylocalvoice
```

### Using virtualenv

```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv pylocalvoice_env

# Activate and install
source pylocalvoice_env/bin/activate  # or pylocalvoice_env\Scripts\activate on Windows
pip install pylocalvoice
```

### Using conda

```bash
# Create conda environment
conda create -n pylocalvoice_env python=3.9

# Activate environment
conda activate pylocalvoice_env

# Install pylocalvoice
pip install pylocalvoice
```

### Using Poetry

```bash
# Initialize project
poetry init

# Add pylocalvoice
poetry add pylocalvoice

# Install
poetry install
```

## Development Installation

For contributing or developing pylocalvoice:

### Step 1: Clone Repository

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Step 3: Install in Editable Mode

```bash
# Install with development dependencies
pip install -e ".[dev]"
```

### Step 4: Verify Installation

```bash
# Run tests
pytest

# Check code quality
make lint

# Format code
make format
```

## Verification

### Check Installation

```bash
pip show pylocalvoice
```

Expected output:
```
Name: pylocalvoice
Version: 0.1.0
Summary: A professional Python library for local voice and Hmong language processing
...
```

### Test Import

```python
python -c "from pylocalvoice from pylocalvoice import pyhmong; print(pyhmong.__version__ if hasattr(pyhmong, '__version__') else '0.1.0')"
```

Expected output:
```
0.1.0
```

### Run Quick Test

```python
python -c "from pylocalvoice from pylocalvoice import pyhmong; print(pyhmong.normalize_text('kuv yog neeg'))"
```

Expected output:
```
Kuv yog neeg
```

### Run Example Script

```bash
python examples.py
```

## Troubleshooting

### Issue: pip not found

**Solution:**

```bash
# Install pip
python -m ensurepip --upgrade

# Or on Linux
sudo apt install python3-pip  # Ubuntu/Debian
sudo dnf install python3-pip  # Fedora
```

### Issue: Permission Denied

**Solution 1: Use --user flag**

```bash
pip install --user pylocalvoice
```

**Solution 2: Use virtual environment** (Recommended)

```bash
python -m venv venv
source venv/bin/activate
pip install pylocalvoice
```

**Solution 3: Use sudo** (Not recommended)

```bash
sudo pip install pylocalvoice
```

### Issue: Old Python Version

**Error:** `pyhmong requires Python '>=3.7'`

**Solution:**

```bash
# Check Python version
python --version

# Install newer Python version
# Ubuntu/Debian
sudo apt install python3.9

# macOS (using Homebrew)
brew install python@3.9

# Windows: Download from python.org
```

### Issue: SSL Certificate Error

**Solution:**

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pyhmong
```

### Issue: Proxy Settings

**Solution:**

```bash
pip install --proxy http://user:password@proxy-server:port pyhmong
```

### Issue: Import Error After Installation

**Problem:**
```python
ImportError: No module named 'pyhmong'
```

**Solutions:**

1. Check if installed in correct environment:
```bash
pip list | grep pyhmong
```

2. Verify Python interpreter:
```bash
which python
which pip
```

3. Reinstall:
```bash
pip uninstall pyhmong
pip install pylocalvoice
```

### Issue: Conflicting Dependencies

**Solution:**

```bash
# Create fresh virtual environment
python -m venv fresh_env
source fresh_env/bin/activate
pip install pylocalvoice
```

## Upgrading

### Upgrade to Latest Version

```bash
pip install --upgrade pyhmong
```

### Upgrade to Specific Version

```bash
pip install --upgrade pyhmong==0.2.0
```

### Check for Updates

```bash
pip list --outdated | grep pyhmong
```

## Uninstallation

### Remove Package

```bash
pip uninstall pyhmong
```

### Remove with Dependencies

```bash
pip uninstall pyhmong
# Manually check and remove unused dependencies
pip list
```

### Complete Cleanup

```bash
# Uninstall package
pip uninstall pyhmong

# Remove cache
pip cache purge

# Remove virtual environment (if used)
rm -rf venv/  # or rmdir /s venv on Windows
```

## Installation for Different Use Cases

### For End Users

```bash
pip install pylocalvoice
```

### For Developers

```bash
git clone https://github.com/yourusername/pyhmong.git
cd pyhmong
pip install -e ".[dev]"
```

### For CI/CD

```yaml
# .github/workflows/example.yml
- name: Install pyhmong
  run: |
    pip install pylocalvoice
```

### For Docker

```dockerfile
FROM python:3.9-slim
RUN pip install pylocalvoice
```

### For Jupyter Notebooks

```bash
# In notebook cell
!pip install pylocalvoice

# Then import
from pylocalvoice import pyhmong
```

## Checking Installation Health

### Run All Checks

```bash
# Check installation
pip show pyhmong

# Test import
python -c "from pylocalvoice import pyhmong"

# Run example
python -c "from pylocalvoice import pyhmong; print(pyhmong.tokenize('test'))"

# Check version
python -c "from pylocalvoice import pyhmong; print(pyhmong.__version__)"
```

### Detailed Diagnostics

```python
import sys
from pylocalvoice import pyhmong

print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")
print(f"pyhmong version: {pyhmong.__version__}")
print(f"pyhmong location: {pyhmong.__file__}")
print("\nAvailable functions:")
print(dir(pyhmong))
```

## Getting Help

If you encounter issues:

1. **Check Documentation**: [README.md](README.md)
2. **Search Issues**: [GitHub Issues](https://github.com/yangnobody12/pylocalvoice/issues)
3. **Ask Questions**: [GitHub Discussions](https://github.com/yangnobody12/pylocalvoice/discussions)
4. **Contact**: yangnobody12@example.com

## Next Steps

After successful installation:

1. Read the [Quick Start Guide](QUICKSTART.md)
2. Try the [Examples](examples.py)
3. Explore the [API Documentation](README.md#api-reference)
4. Join the community and contribute!

---

**Installation successful?** Start using pyhmong:

```python
from pylocalvoice import pyhmong

text = "Kuv yog neeg Hmoob"
tokens = pyhmong.tokenize(text)
print(tokens)
```

Happy coding! 🎉