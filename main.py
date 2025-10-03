#!/usr/bin/env python3
"""
PyHmong Project Generator
Creates complete pyhmong library structure with all files
"""

import os
import sys

def create_directory_structure():
    """Create all necessary directories."""
    dirs = [
        'pyhmong/data',
        'tests',
        '.github/workflows',
        'docs'
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"✅ Created: {dir_path}/")

def print_instructions():
    """Print instructions for completing the setup."""
    instructions = """
╔════════════════════════════════════════════════════════════╗
║              PyHmong Project Generator                     ║
╚════════════════════════════════════════════════════════════╝

✅ Directory structure created successfully!

📋 Files you need to copy from Claude's artifacts:

┌─ Main Package ─────────────────────────────────────────┐
│ 1.  pyhmong/__init__.py        (from "Package Init")   │
│ 2.  pyhmong/core.py            (from "Main Module")    │
└────────────────────────────────────────────────────────┘

┌─ Tests ────────────────────────────────────────────────┐
│ 3.  tests/test_pyhmong.py      (from "Unit Tests")     │
└────────────────────────────────────────────────────────┘

┌─ Configuration ────────────────────────────────────────┐
│ 4.  setup.py                   (from "Package Config") │
│ 5.  pyproject.toml             (from "Modern Config")  │
│ 6.  requirements.txt           (from "Dependencies")   │
│ 7.  requirements-dev.txt       (from "Dev Deps")       │
│ 8.  pytest.ini                 (from "Pytest Config")  │
│ 9.  Makefile                   (from "Dev Commands")   │
│ 10. MANIFEST.in                (from "Package Files")  │
│ 11. .gitignore                 (from "Git Ignore")     │
│ 12. LICENSE                    (from "MIT License")    │
└────────────────────────────────────────────────────────┘

┌─ Documentation ────────────────────────────────────────┐
│ 13. README.md                  (from "Documentation")  │
│ 14. QUICKSTART.md              (from "Quick Start")    │
│ 15. INSTALL.md                 (from "Install Guide")  │
│ 16. CONTRIBUTING.md            (from "Contribution")   │
│ 17. CHANGELOG.md               (from "Version Hist")   │
└────────────────────────────────────────────────────────┘

┌─ CI/CD & Examples ─────────────────────────────────────┐
│ 18. .github/workflows/tests.yml (from "CI/CD")        │
│ 19. examples.py                 (from "Examples")      │
└────────────────────────────────────────────────────────┘

🚀 After copying all files:

1. Install the package:
   pip install -e .

2. Run tests:
   pytest

3. Try examples:
   python examples.py

4. Check code quality:
   make lint

5. Format code:
   make format

📚 Quick Reference:

   • All 19 files are shown in Claude's conversation
   • Click "Copy" button on each artifact
   • Paste into corresponding file path
   • Total size: ~50 KB

✨ You're ready to go! Happy coding with pyhmong!
"""
    print(instructions)

def create_placeholder_files():
    """Create placeholder files with instructions."""
    placeholders = {
        'pyhmong/__init__.py': '# TODO: Copy content from artifact "Package Initialization"\n',
        'pyhmong/core.py': '# TODO: Copy content from artifact "Main Module"\n',
        'tests/test_pyhmong.py': '# TODO: Copy content from artifact "Unit Tests"\n',
        'README.md': '# TODO: Copy content from artifact "Documentation"\n',
    }
    
    for filepath, content in placeholders.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"📝 Created placeholder: {filepath}")

def main():
    """Main function."""
    print("🎯 PyHmong Project Generator")
    print("=" * 60)
    print()
    
    # Check if already in a pyhmong directory
    if os.path.exists('pyhmong') and os.path.isdir('pyhmong'):
        response = input("⚠️  'pyhmong' directory already exists. Continue? (y/N): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    
    # Create structure
    print("📁 Creating directory structure...")
    create_directory_structure()
    print()
    
    # Create placeholders
    print("📝 Creating placeholder files...")
    create_placeholder_files()
    print()
    
    # Print instructions
    print_instructions()

if __name__ == '__main__':
    main()