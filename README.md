# PyLocalVoice 🇱🇦

[![PyPI version](https://badge.fury.io/py/pylocalvoice.svg)](https://badge.fury.io/py/pylocalvoice)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A professional Python library for local voice and Hmong language processing. This library provides comprehensive tools for working with the Hmong language, including text processing, translation, grammar analysis, and educational utilities.

## ✨ Features

### 🔤 1. Phonology & Orthography
- **normalize_text()**: Standardize Hmong text (fix tones, case, spacing)
- **syllable_split()**: Split words into syllables (CV + tone structure)
- **get_tone()**: Detect tone markers (-b, -j, -v, -s, -g, -d, -m)
- **convert_tone()**: Convert syllables between different tones

### 📚 2. Dictionary & Translation
- **translate_hm_to_en()**: Translate Hmong → English (Heimbach Dict based)
- **translate_en_to_hm()**: Translate English → Hmong
- **search_dictionary()**: Search with examples and fuzzy matching

### 📖 3. Grammar
- **detect_pos()**: Detect part of speech (noun, verb, classifier, etc.)
- **get_classifiers()**: Get appropriate classifiers for nouns
- **conjugate()**: Add tense markers (past, present, future)
- **substitute()**: Grammar drill exercises

### 💬 4. Phrasebook Utilities
- **get_greeting()**: Get greetings (morning, afternoon, evening)
- **ask_question()**: Common questions (name, age, location, etc.)
- **basic_dialogue()**: Pre-built dialogues by topic (food, family, etc.)

### 🔢 5. Numbers & Measures
- **num_to_hmong()**: Convert numbers to Hmong words (1 = ib, 2 = ob)
- **hmong_to_num()**: Convert Hmong words to numbers
- **convert_measure()**: Unit conversions (lbs ↔ kg, miles ↔ km)

### 💭 6. Proverbs & Idioms
- **get_proverb()**: Get Hmong proverbs by topic
- **explain_idiom()**: Explain cultural expressions and meanings

### 🎓 7. Education Tools
- **generate_drill()**: Create pronunciation drills (tone, consonant, vowel)
- **quiz_flashcards()**: Flashcard sets by category (food, family, colors)
- **check_pronunciation()**: Analyze syllable structure and pronunciation

## 📦 Installation

### From PyPI (Recommended)

```bash
pip install pylocalvoice
```

### From Source

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
pip install -e .
```

### For Development

```bash
git clone https://github.com/yangnobody12/pylocalvoice.git
cd pylocalvoice
pip install -e ".[dev]"
```

## 🚀 Quick Start

```python
from pylocalvoice import pyhmong

# 1. Phonology - Normalize and analyze text
text = "kuv  YOG  neeg"
clean = pyhmong.normalize_text(text)  # "Kuv yog neeg"
tone = pyhmong.get_tone("kuv")  # "V"
converted = pyhmong.convert_tone("kuv", "b")  # "kub"

# 2. Translation - Hmong ↔ English
pyhmong.translate_hm_to_en("niam")  # "mother"
pyhmong.translate_en_to_hm("father")  # "txiv"

# 3. Grammar - Analyze and conjugate
pyhmong.detect_pos("yog")  # "verb"
pyhmong.get_classifiers("neeg")  # ["tus"]
pyhmong.conjugate("Kuv mus tsev", "past")  # "Kuv mus tsev lawm"

# 4. Phrasebook - Common phrases
pyhmong.get_greeting("morning")  # "Nyob zoo sawv ntxov"
pyhmong.ask_question("name")  # "Koj lub npe hu li cas?"

# 5. Numbers - Convert numbers
pyhmong.num_to_hmong(5)  # "tsib"
pyhmong.hmong_to_num("kaum")  # 10

# 6. Proverbs - Cultural expressions
pyhmong.get_proverb("wisdom")  # Returns Hmong proverb

# 7. Education - Learning tools
pyhmong.generate_drill("tone")  # ['pab', 'paj', 'pav', ...]
pyhmong.quiz_flashcards("food")  # {'mov': 'rice', ...}
```

## 📚 Documentation

- **[Features Guide](FEATURES.md)** - Complete guide to all 7 feature categories
- **[Quick Start](QUICKSTART.md)** - Get started in 5 minutes
- **[Installation Guide](INSTALL.md)** - Detailed installation instructions
- **[Contributing](CONTRIBUTING.md)** - How to contribute
- **[Changelog](CHANGELOG.md)** - Version history

## 💡 Use Cases

### Language Learning
```python
from pylocalvoice import pyhmong

# Learn basic greetings
print(pyhmong.get_greeting("morning"))  # "Nyob zoo sawv ntxov"

# Practice pronunciation with drills
drills = pyhmong.generate_drill("tone")
for drill in drills:
    print(f"Practice: {drill}")

# Quiz yourself with flashcards
cards = pyhmong.quiz_flashcards("food")
```

### Text Processing
```python
from pylocalvoice import pyhmong

# Clean up messy Hmong text
messy = "kuv   YOG  neeg   HMOOB"
clean = pyhmong.normalize_text(messy)  # "Kuv yog neeg hmoob"

# Analyze syllable structure
analysis = pyhmong.check_pronunciation("ntxawg")
print(analysis)  # Shows onset, nucleus, tone
```

### Translation & Dictionary
```python
from pylocalvoice import pyhmong

# Build a vocabulary list
words = ["niam", "txiv", "tub", "ntxhais"]
for word in words:
    english = pyhmong.translate_hm_to_en(word)
    print(f"{word} = {english}")

# Search for related words
results = pyhmong.search_dictionary("family", lang="en")
```

### Grammar Practice
```python
from pylocalvoice import pyhmong

# Practice tenses
sentence = "Kuv mus tsev"
print(pyhmong.conjugate(sentence, "past"))    # Add past marker
print(pyhmong.conjugate(sentence, "future"))  # Add future marker

# Learn classifiers
print(pyhmong.get_classifiers("neeg"))  # ["tus"]
print(pyhmong.get_classifiers("tsev"))  # ["lub"]
```

## 🎯 API Overview

### Quick Reference

```python
from pylocalvoice import pyhmong

# === PHONOLOGY ===
pyhmong.normalize_text(text)          # Clean text
pyhmong.get_tone(syllable)            # Get tone marker
pyhmong.convert_tone(syl, tone)       # Change tone
pyhmong.syllable_split(word)          # Split syllables

# === TRANSLATION ===
pyhmong.translate_hm_to_en(word)      # Hmong → English
pyhmong.translate_en_to_hm(word)      # English → Hmong
pyhmong.search_dictionary(query)      # Search both ways

# === GRAMMAR ===
pyhmong.detect_pos(word)              # Part of speech
pyhmong.get_classifiers(noun)         # Get classifiers
pyhmong.conjugate(sent, tense)        # Add tense
pyhmong.substitute(sent, old, new)    # Replace words

# === PHRASEBOOK ===
pyhmong.get_greeting(time)            # Greetings
pyhmong.ask_question(topic)           # Questions
pyhmong.basic_dialogue(unit)          # Dialogues

# === NUMBERS ===
pyhmong.num_to_hmong(n)               # 5 → "tsib"
pyhmong.hmong_to_num(word)            # "ib" → 1
pyhmong.convert_measure(val, f, t)    # Unit conversion

# === PROVERBS ===
pyhmong.get_proverb(topic)            # Get proverb
pyhmong.explain_idiom(phrase)         # Explain idiom

# === EDUCATION ===
pyhmong.generate_drill(type)          # Pronunciation drills
pyhmong.quiz_flashcards(category)     # Flashcards
pyhmong.check_pronunciation(word)     # Check structure
```

## 🔧 Advanced Usage

### Batch Processing

```python
from pylocalvoice import pyhmong

# Process multiple texts
texts = [
    "Kuv yog neeg Hmoob",
    "Koj nyob li cas?",
    "Peb mus tsev"
]

for text in texts:
    clean = pyhmong.normalize_text(text)

    print(f"Text: {text}")
    print(f"Clean: {clean}")

    # Translate each word
    for word in clean.split():
        translation = pyhmong.translate_hm_to_en(word)
        print(f"  {word} = {translation}")
    print()
```

## 📊 Statistics

- **22 main functions** across 7 categories
- **100+ Hmong words** in dictionary
- **8 tone markers** supported
- **40+ consonants** (including digraphs and trigraphs)
- **15+ vowels** (simple and complex)
- **3 dialogue units** with 12+ phrases
- **3 flashcard categories** (food, family, colors)

## 🗺️ Roadmap

### Version 0.2.0 (Planned)
- [ ] Extended dictionary (1000+ words)
- [ ] Pahawh Hmong script support
- [ ] Audio pronunciation guide
- [ ] More dialogue units (10+ topics)

### Version 0.3.0 (Future)
- [ ] White Hmong vs Green Hmong dialect support
- [ ] Text-to-speech integration
- [ ] Advanced grammar parser
- [ ] Named entity recognition

### Version 1.0.0 (Long-term)
- [ ] Machine translation
- [ ] Language detection
- [ ] Part-of-speech tagger (full)
- [ ] Web API wrapper
- [ ] Mobile app support

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
- Add more words to dictionary
- Create new dialogue units
- Add proverbs and idioms
- Improve pronunciation drills
- Write documentation
- Report bugs
- Suggest features

## 📖 Resources

### Learn More About Hmong Language

- [Hmong Language Wikipedia](https://en.wikipedia.org/wiki/Hmong_language)
- [RPA Romanization System](https://en.wikipedia.org/wiki/Romanized_Popular_Alphabet)
- [Heimbach Hmong Dictionary](https://en.wikipedia.org/wiki/Ernest_E._Heimbach)

### Related Projects

- [Hmong Dictionary Online](https://hmongdictionary.com)
- [White Hmong Resources](https://en.wikipedia.org/wiki/Hmong_language#White_Hmong)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the Hmong community for preserving this beautiful language
- Based on Ernest E. Heimbach's White Hmong-English Dictionary
- Inspired by various NLP libraries and linguistic research
- Built with modern Python best practices

## 📧 Contact & Support

- **Author**: YangNobody12
- **Email**: pkorn8394@gmail.com
- **PyPI**: https://pypi.org/project/pylocalvoice/
- **Issues**: [GitHub Issues](https://github.com/yangnobody12/pylocalvoice/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yangnobody12/pylocalvoice/discussions)

## ⭐ Show Your Support

If you find this library helpful, please consider:
- Starring the repository ⭐
- Sharing with others who learn Hmong
- Contributing to the project
- Reporting issues and suggesting features

## 📝 Citation

If you use this library in your research or project, please cite:

```bibtex
@software{pylocalvoice,
  author = {YangNobody12},
  title = {PyLocalVoice: A Comprehensive Python Library for Hmong Language Processing},
  year = {2025},
  url = {https://github.com/yangnobody12/pylocalvoice},
  version = {0.1.0}
}
```

---

**Made with ❤️ for the Hmong community**

*Ua tsaug! (Thank you!)*
