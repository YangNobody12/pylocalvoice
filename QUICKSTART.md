# PyLocalVoice Quick Start Guide

Get started with pylocalvoice in 5 minutes! 🚀

## Installation

```bash
pip install pylocalvoice
```

Or from source:

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
pip install -e .
```

## Basic Usage

### 1. Import the library

```python
from pylocalvoice import pyhmong
```

### 2. Normalize Hmong text

```python
text = "kuv   yog  NEEG   hmoob"
clean = pyhmong.normalize_text(text)
print(clean)
# Output: "Kuv yog neeg hmoob"
```

### 3. Translate words

```python
print(pyhmong.translate_hm_to_en("niam"))   # "mother"
print(pyhmong.translate_en_to_hm("father")) # "txiv"
```

### 4. Get greetings

```python
greeting = pyhmong.get_greeting("morning")
print(greeting)
# Output: "Nyob zoo sawv ntxov"
```

## Advanced Usage

### Using Translation

```python
from pylocalvoice import pyhmong

# Hmong to English
print(pyhmong.translate_hm_to_en("kuv"))    # "I, me"
print(pyhmong.translate_hm_to_en("koj"))    # "you (singular)"

# English to Hmong
print(pyhmong.translate_en_to_hm("mother")) # "niam"
print(pyhmong.translate_en_to_hm("father")) # "txiv"
```

### Using Grammar

```python
from pylocalvoice import pyhmong

# Detect part of speech
print(pyhmong.detect_pos("kuv"))    # "pronoun"
print(pyhmong.detect_pos("yog"))    # "verb"

# Get classifiers
print(pyhmong.get_classifiers("neeg"))  # ["tus"]

# Conjugate tenses
sentence = "Kuv mus tsev"
print(pyhmong.conjugate(sentence, "past"))   # "Kuv mus tsev lawm"
print(pyhmong.conjugate(sentence, "future")) # "yuav Kuv mus tsev"
```

## Common Use Cases

### Example 1: Language Learning

```python
from pylocalvoice import pyhmong

# Get greetings
print(pyhmong.get_greeting("morning"))   # "Nyob zoo sawv ntxov"
print(pyhmong.get_greeting("evening"))   # "Nyob zoo tsaus ntuj"

# Ask questions
print(pyhmong.ask_question("name"))      # "Koj lub npe hu li cas?"
print(pyhmong.ask_question("age"))       # "Koj muaj pes tsawg xyoos?"
```

### Example 2: Translation

```python
from pylocalvoice import pyhmong

# Build vocabulary
family_words = ["niam", "txiv", "tub", "ntxhais"]
for word in family_words:
    english = pyhmong.translate_hm_to_en(word)
    print(f"{word} = {english}")
```

### Example 3: Numbers

```python
from pylocalvoice import pyhmong

# Convert numbers to Hmong
for i in range(1, 11):
    hmong_num = pyhmong.num_to_hmong(i)
    print(f"{i} = {hmong_num}")
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
ImportError: No module named 'pylocalvoice'
```

**Solution:**
```bash
pip install pylocalvoice
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

- **Documentation**: https://pylocalvoice.readthedocs.io
- **GitHub**: https://github.com/yangnobody12/pylocalvoice
- **Issues**: https://github.com/yangnobody12/pylocalvoice/issues
- **PyPI**: https://pypi.org/project/pylocalvoice

## Need Help?

- 📖 Check the [full documentation](README.md)
- 💬 Ask in [GitHub Discussions](https://github.com/yangnobody12/pylocalvoice/discussions)
- 🐛 Report bugs in [Issues](https://github.com/yangnobody12/pylocalvoice/issues)
- 📧 Email: pkorn8394@gmail.com

Happy coding with pylocalvoice! 🎉