# pyhmong Quick Start Guide

Get started with pyhmong in 5 minutes! 🚀

## Installation

```bash
pip install pyhmong
```

Or from source:

```bash
git clone https://github.com/yourusername/pyhmong.git
cd pyhmong
pip install -e .
```

## Basic Usage

### 1. Import the library

```python
import pyhmong
```

### 2. Tokenize Hmong text

```python
text = "Kuv yog neeg Hmoob"
tokens = pyhmong.tokenize(text)
print(tokens)
# Output: ['Kuv', 'yog', 'neeg', 'Hmoob']
```

### 3. Validate Hmong syllables

```python
print(pyhmong.is_valid_syllable("kuv"))   # True
print(pyhmong.is_valid_syllable("xyz"))   # False
```

### 4. Normalize text

```python
messy = "kuv   yog  NEEG   hmoob"
clean = pyhmong.normalize(messy)
print(clean)
# Output: "Kuv yog neeg hmoob"
```

## Advanced Usage

### Using HmongProcessor

```python
from pyhmong import HmongProcessor

processor = HmongProcessor()

# Get tone information
tone = processor.get_tone("kuv")
print(tone)  # ToneMarker.V: 'mid-high rising tone'

# Decompose syllable
parts = processor.decompose_syllable("ntxawg")
print(parts)
# Output: {'onset': 'ntx', 'nucleus': 'aw', 'coda': 'g'}

# Count syllables
count = processor.count_syllables("Nyob zoo koj nyob li cas")
print(count)  # 6
```

### Using Dictionary

```python
from pyhmong import HmongDictionary

dictionary = HmongDictionary()

# Look up words
meaning = dictionary.lookup("kuv")
print(meaning)  # "I, me"

# Add custom words
dictionary.add_word("tsev", "house")
print(dictionary.lookup("tsev"))  # "house"
```

## Common Use Cases

### Example 1: Text Analysis

```python
from pyhmong import HmongProcessor

processor = HmongProcessor()
text = "Nyob zoo, koj nyob li cas?"

# Analyze the text
tokens = processor.tokenize(text)
print(f"Tokens: {tokens}")

for token in tokens:
    if processor.is_valid_syllable(token):
        tone = processor.get_tone(token)
        print(f"{token}: {tone.name}")
```

### Example 2: Data Cleaning

```python
import pyhmong

# Clean messy Hmong text
texts = [
    "kuv   YOG  neeg",
    "KOJ    nyob  QHOV  twg",
    "peb   mus   TSEV"
]

for text in texts:
    clean = pyhmong.normalize(text)
    print(f"Before: '{text}'")
    print(f"After:  '{clean}'")
    print()
```

### Example 3: Syllable Validation

```python
from pyhmong import HmongProcessor

processor = HmongProcessor()

# Validate a list of words
words = ["kuv", "koj", "hello", "ntxawg", "xyz"]

for word in words:
    valid = processor.is_valid_syllable(word)
    status = "✓" if valid else "✗"
    print(f"{status} {word}")
```

## Next Steps

- Read the full [README](README.md) for detailed documentation
- Check out [examples.py](examples.py) for more examples
- Explore the API reference in the documentation
- Contribute at [CONTRIBUTING.md](CONTRIBUTING.md)

## Common Issues

### Issue: Import Error

**Problem:**
```python
ImportError: No module named 'pyhmong'
```

**Solution:**
```bash
pip install pyhmong
# or
pip install -e .  # if installing from source
```

### Issue: Invalid Syllable Not Detected

**Problem:** A syllable that should be invalid returns True

**Solution:** The RPA system has complex rules. Check the documentation for valid syllable patterns.

### Issue: Tone Not Recognized

**Problem:** `get_tone()` returns `NONE` for a syllable with a tone marker

**Solution:** Make sure the tone marker is at the end of the syllable (b, j, v, s, g, d, m).

## Resources

- **Documentation**: https://pyhmong.readthedocs.io
- **GitHub**: https://github.com/yangnobody12/pyhmong
- **Issues**: https://github.com/yangnobody12/pyhmong/issues
- **PyPI**: https://pypi.org/project/pyhmong

## Need Help?

- 📖 Check the [full documentation](README.md)
- 💬 Ask in [GitHub Discussions](https://github.com/yangnobody12/pyhmong/discussions)
- 🐛 Report bugs in [Issues](https://github.com/yangnobody12/pyhmong/issues)
- 📧 Email: pkorn8394@gmail.com

Happy coding with pyhmong! 🎉