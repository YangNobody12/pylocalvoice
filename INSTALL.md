# Installation Guide for pyhmong

This guide covers all the ways to install pyhmong on your system.

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

pyhmong has **no external dependencies** for core functionality! It uses only Python's standard library.

## Installation Methods

### Method 1: Install from PyPI (Recommended)

Once published, install using pip:

```bash
pip install pyhmong
```

To install a specific version:

```bash
pip install pyhmong==0.1.0
```

### Method 2: Install from Source

#### Using pip

```bash
git clone https://github.com/yangnobody12/pyhmong.git
cd pyhmong
pip install .
```

#### For Development

```bash
git clone https://github.com/yangnobody12/pyhmong.git
cd pyhmong
pip install -e ".[dev]"
```

### Method 3: Download and Install

1. Download the latest release from [GitHub Releases](https://github.com/yangnobody12/pyhmong/releases)
2. Extract the archive
3. Navigate to the directory
4. Install:

```bash
cd pyhmong-0.1.0
pip install .
```

### Method 4: Using pipx (Isolated Environment)

```bash
pipx install pyhmong
```

## Platform-Specific Instructions

### Windows

#### Using Command Prompt

```cmd
python -m pip install pyhmong
```

#### Using PowerShell

```powershell
python -m pip install pyhmong
```

#### Using Anaconda

```bash
conda activate your_environment
pip install pyhmong
```

### macOS

#### Using Terminal

```bash
pip3 install pyhmong
```

#### Using Homebrew Python

```bash
/usr/local/bin/pip3 install pyhmong
```

### Linux

#### Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3-pip
pip3 install pyhmong
```

#### Fedora/RHEL/CentOS

```bash
sudo dnf install python3-pip
pip3 install pyhmong
```

#### Arch Linux

```bash
sudo pacman -S python-pip
pip install pyhmong
```

## Virtual Environments

### Using venv (Recommended)

```bash
# Create virtual environment
python -m venv pyhmong_env

# Activate on Windows
pyhmong_env\Scripts\activate

# Activate on macOS/Linux
source pyhmong_env/bin/activate

# Install pyhmong
pip install pyhmong
```

### Using virtualenv

```bash
# Install virtualenv
pip install virtualenv

# Create environment
virtualenv pyhmong_env

# Activate and install
source pyhmong_env/bin/activate  # or pyhmong_env\Scripts\activate on Windows
pip install pyhmong
```

### Using conda

```bash
# Create conda environment
conda create -n pyhmong_env python=3.9

# Activate environment
conda activate pyhmong_env

# Install pyhmong
pip install pyhmong
```

### Using Poetry

```bash
# Initialize project
poetry init

# Add pyhmong
poetry add pyhmong

# Install
poetry install
```

## Development Installation

For contributing or developing pyhmong:

### Step 1: Clone Repository

```bash
git clone https://github.com/yangnobody12/pyhmong.git
cd pyhmong
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
pip show pyhmong
```

Expected output:
```
Name: pyhmong
Version: 0.1.0
Summary: A professional Python library for Hmong language processing
...
```

### Test Import

```python
python -c "import pyhmong; print(pyhmong.__version__)"
```

Expected output:
```
0.1.0
```

### Run Quick Test

```python
python -c "import pyhmong; print(pyhmong.tokenize('Kuv yog neeg Hmoob'))"
```

Expected output:
```
['Kuv', 'yog', 'neeg', 'Hmoob']
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
pip install --user pyhmong
```

**Solution 2: Use virtual environment** (Recommended)

```bash
python -m venv venv
source venv/bin/activate
pip install pyhmong
```

**Solution 3: Use sudo** (Not recommended)

```bash
sudo pip install pyhmong
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
pip install pyhmong
```

### Issue: Conflicting Dependencies

**Solution:**

```bash
# Create fresh virtual environment
python -m venv fresh_env
source fresh_env/bin/activate
pip install pyhmong
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
pip install pyhmong
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
    pip install pyhmong
```

### For Docker

```dockerfile
FROM python:3.9-slim
RUN pip install pyhmong
```

### For Jupyter Notebooks

```bash
# In notebook cell
!pip install pyhmong

# Then import
import pyhmong
```

## Checking Installation Health

### Run All Checks

```bash
# Check installation
pip show pyhmong

# Test import
python -c "import pyhmong"

# Run example
python -c "import pyhmong; print(pyhmong.tokenize('test'))"

# Check version
python -c "import pyhmong; print(pyhmong.__version__)"
```

### Detailed Diagnostics

```python
import sys
import pyhmong

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
2. **Search Issues**: [GitHub Issues](https://github.com/yangnobody12/pyhmong/issues)
3. **Ask Questions**: [GitHub Discussions](https://github.com/yangnobody12/pyhmong/discussions)
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
import pyhmong

text = "Kuv yog neeg Hmoob"
tokens = pyhmong.tokenize(text)
print(tokens)
```

Happy coding! 🎉