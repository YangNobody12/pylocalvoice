# PyHmong Features Guide

Complete guide to all 7 feature categories in pyhmong library.

---

## 📋 Table of Contents

1. [Phonology & Orthography](#1-phonology--orthography)
2. [Dictionary & Translation](#2-dictionary--translation)
3. [Grammar](#3-grammar)
4. [Phrasebook Utilities](#4-phrasebook-utilities)
5. [Numbers & Measures](#5-numbers--measures)
6. [Proverbs & Idioms](#6-proverbs--idioms)
7. [Education Tools](#7-education-tools)

---

## 1. Phonology & Orthography

Tools for handling Hmong text normalization, syllable structure, and tone analysis.

### `normalize_text(text: str) -> str`

Standardize Hmong text formatting.

**Features:**
- Fix tone markers
- Standardize case (capitalize first word)
- Remove extra spacing

**Example:**
```python
import pyhmong

text = "kuv   YOG  neeg   HMOOB"
clean = pyhmong.normalize_text(text)
print(clean)  # "Kuv yog neeg hmoob"
```

### `syllable_split(word: str) -> list[str]`

Split words into syllables based on CV + tone structure.

**Example:**
```python
word = "Hmoob"
syllables = pyhmong.syllable_split(word)
print(syllables)  # ['Hmoob']
```

### `get_tone(syllable: str) -> str`

Detect tone marker of a syllable.

**Hmong Tones:**
- `b` = mid-low tone
- `j` = high falling tone
- `v` = mid-high rising tone
- `s` = low breathy tone
- `g` = low falling tone
- `d` = high tone
- `m` = low glottalized tone
- `NONE` = mid tone (unmarked)

**Example:**
```python
print(pyhmong.get_tone("kuv"))   # "V"
print(pyhmong.get_tone("koj"))   # "J"
print(pyhmong.get_tone("zoo"))   # "NONE"
```

### `convert_tone(syllable: str, target_tone: str) -> str`

Convert syllable to different tone.

**Example:**
```python
original = "kuv"
print(pyhmong.convert_tone(original, "b"))  # "kub"
print(pyhmong.convert_tone(original, "j"))  # "kuj"
print(pyhmong.convert_tone(original, "s"))  # "kus"
```

---

## 2. Dictionary & Translation

Hmong ↔ English translation based on Heimbach Dictionary.

### `translate_hm_to_en(word: str) -> str`

Translate Hmong word to English.

**Example:**
```python
print(pyhmong.translate_hm_to_en("niam"))   # "mother"
print(pyhmong.translate_hm_to_en("txiv"))   # "father"
print(pyhmong.translate_hm_to_en("tsev"))   # "house, home"
```

### `translate_en_to_hm(word: str) -> str | list[str]`

Translate English word to Hmong.

**Example:**
```python
print(pyhmong.translate_en_to_hm("mother"))  # "niam"
print(pyhmong.translate_en_to_hm("father"))  # "txiv"
print(pyhmong.translate_en_to_hm("I"))       # "kuv"
```

### `search_dictionary(query: str, lang="hm"|"en") -> list`

Search dictionary with fuzzy matching.

**Example:**
```python
# Search Hmong words
results = pyhmong.search_dictionary("niam", lang="hm")
for result in results:
    print(f"{result['hmong']} = {result['english']}")

# Search English words
results = pyhmong.search_dictionary("mother", lang="en")
```

---

## 3. Grammar

Grammar analysis and manipulation tools.

### `detect_pos(word: str) -> str`

Detect part of speech.

**Supported POS:**
- noun
- verb
- adjective
- classifier
- pronoun
- preposition
- conjunction
- particle
- adverb

**Example:**
```python
print(pyhmong.detect_pos("kuv"))    # "pronoun"
print(pyhmong.detect_pos("yog"))    # "verb"
print(pyhmong.detect_pos("tus"))    # "classifier"
print(pyhmong.detect_pos("neeg"))   # "noun"
```

### `get_classifiers(noun: str) -> list[str]`

Get appropriate classifiers for a noun.

**Common Classifiers:**
- `tus` - for people, animals
- `lub` - for objects, houses
- `txoj` - for roads, ways
- `daim` - for flat objects

**Example:**
```python
print(pyhmong.get_classifiers("neeg"))  # ["tus"]
print(pyhmong.get_classifiers("tsev"))  # ["lub"]
print(pyhmong.get_classifiers("dev"))   # ["tus"]
```

### `conjugate(sentence: str, tense="past"|"present"|"future") -> str`

Add tense markers to sentences.

**Example:**
```python
sentence = "Kuv mus tsev"

print(pyhmong.conjugate(sentence, "present"))  # "Kuv mus tsev"
print(pyhmong.conjugate(sentence, "past"))     # "Kuv mus tsev lawm"
print(pyhmong.conjugate(sentence, "future"))   # "yuav Kuv mus tsev"
```

### `substitute(sentence: str, target: str, replacement: str) -> str`

Substitute words in sentence (grammar drill).

**Example:**
```python
sentence = "Kuv yog neeg Hmoob"
result = pyhmong.substitute(sentence, "Kuv", "Koj")
print(result)  # "Koj yog neeg Hmoob"
```

---

## 4. Phrasebook Utilities

Common phrases and dialogues for everyday communication.

### `get_greeting(time="morning"|"afternoon"|"evening"|"general") -> str`

Get appropriate greeting for time of day.

**Example:**
```python
print(pyhmong.get_greeting("general"))    # "Nyob zoo"
print(pyhmong.get_greeting("morning"))    # "Nyob zoo sawv ntxov"
print(pyhmong.get_greeting("afternoon"))  # "Nyob zoo tav su"
print(pyhmong.get_greeting("evening"))    # "Nyob zoo tsaus ntuj"
```

### `ask_question(topic: str) -> str`

Get common question phrases.

**Available Topics:**
- `name` - "What is your name?"
- `age` - "How old are you?"
- `from` - "Where are you from?"
- `doing` - "What are you doing?"
- `feeling` - "How are you?"
- `where` - "Where are you?"

**Example:**
```python
print(pyhmong.ask_question("name"))     # "Koj lub npe hu li cas?"
print(pyhmong.ask_question("age"))      # "Koj muaj pes tsawg xyoos?"
print(pyhmong.ask_question("feeling"))  # "Koj nyob li cas?"
```

### `basic_dialogue(unit: int) -> list[tuple[str, str]]`

Get pre-built dialogues by topic.

**Units:**
- Unit 1: Introductions
- Unit 2: Food
- Unit 3: Family

**Example:**
```python
dialogue = pyhmong.basic_dialogue(1)
for hmong, english in dialogue:
    print(f"{hmong}")
    print(f"  → {english}\n")
```

---

## 5. Numbers & Measures

Number conversion and measurement tools.

### `num_to_hmong(n: int) -> str`

Convert numbers to Hmong words.

**Example:**
```python
print(pyhmong.num_to_hmong(1))    # "ib"
print(pyhmong.num_to_hmong(5))    # "tsib"
print(pyhmong.num_to_hmong(10))   # "kaum"
print(pyhmong.num_to_hmong(15))   # "kaum tsib"
print(pyhmong.num_to_hmong(100))  # "ib pua"
```

### `hmong_to_num(word: str) -> int`

Convert Hmong words to numbers.

**Example:**
```python
print(pyhmong.hmong_to_num("ib"))        # 1
print(pyhmong.hmong_to_num("kaum"))      # 10
print(pyhmong.hmong_to_num("kaum ob"))   # 12
```

### `convert_measure(value: float, from_unit: str, to_unit: str) -> str`

Convert between measurement units.

**Supported Conversions:**
- `lbs` ↔ `kg`
- `miles` ↔ `km`
- `feet` ↔ `meters`

**Example:**
```python
print(pyhmong.convert_measure(10, "lbs", "kg"))
# "10 lbs = 4.54 kg"

print(pyhmong.convert_measure(5, "miles", "km"))
# "5 miles = 8.05 km"
```

---

## 6. Proverbs & Idioms

Hmong cultural expressions and sayings.

### `get_proverb(topic="wisdom"|"family"|"work") -> str`

Get Hmong proverb by topic.

**Example:**
```python
print(pyhmong.get_proverb("wisdom"))
# "Niam txiv lus yog lus qhuab qhia"

print(pyhmong.get_proverb("family"))
# "Niam txiv siab zoo, me nyuam thiaj li zoo"
```

### `explain_idiom(phrase: str) -> str`

Explain idiom meaning.

**Example:**
```python
print(pyhmong.explain_idiom("zoo siab"))
# "happy (lit: good heart)"

print(pyhmong.explain_idiom("siab phem"))
# "mean, evil (lit: bad heart)"

print(pyhmong.explain_idiom("siab ntev"))
# "patient (lit: long heart)"
```

---

## 7. Education Tools

Tools for learning and teaching Hmong.

### `generate_drill(type="tone"|"consonant"|"vowel") -> list[str]`

Generate pronunciation practice drills.

**Example:**
```python
# Tone drill
print(pyhmong.generate_drill("tone"))
# ['pab', 'paj', 'pav', 'pas', 'pag', 'pad', 'pam', 'pa']

# Consonant drill
print(pyhmong.generate_drill("consonant"))
# ['peb', 'keb', 'teb', 'neb', 'meb']

# Vowel drill
print(pyhmong.generate_drill("vowel"))
# ['pa', 'pe', 'pi', 'po', 'pu']
```

### `quiz_flashcards(category="food"|"family"|"colors") -> dict`

Get flashcard sets for quiz.

**Example:**
```python
# Food vocabulary
cards = pyhmong.quiz_flashcards("food")
for hmong, english in cards.items():
    print(f"{hmong} = {english}")
# mov = rice
# nqaij = meat
# zaub = vegetables

# Family vocabulary
cards = pyhmong.quiz_flashcards("family")
```

### `check_pronunciation(word: str) -> dict`

Analyze word pronunciation structure.

**Example:**
```python
analysis = pyhmong.check_pronunciation("kuv")
print(analysis)
# {
#   'word': 'kuv',
#   'valid': True,
#   'onset': 'k',
#   'nucleus': 'u',
#   'tone': 'V',
#   'feedback': 'Valid Hmong syllable'
# }
```

---

## Complete Example

Here's a complete example using multiple features:

```python
import pyhmong

# 1. Normalize text
text = "kuv  yog  NEEG  hmoob"
clean = pyhmong.normalize_text(text)
print(f"Cleaned: {clean}")

# 2. Translate words
for word in clean.split():
    translation = pyhmong.translate_hm_to_en(word)
    print(f"{word} = {translation}")

# 3. Check grammar
pos = pyhmong.detect_pos("kuv")
print(f"'kuv' is a {pos}")

# 4. Practice greetings
greeting = pyhmong.get_greeting("morning")
print(f"Morning greeting: {greeting}")

# 5. Learn numbers
for i in range(1, 6):
    hmong_num = pyhmong.num_to_hmong(i)
    print(f"{i} = {hmong_num}")

# 6. Get wisdom
proverb = pyhmong.get_proverb("wisdom")
print(f"Proverb: {proverb}")

# 7. Practice pronunciation
drill = pyhmong.generate_drill("tone")
print(f"Practice: {drill}")
```

---

## Feature Summary

| Category | Functions | Purpose |
|----------|-----------|---------|
| Phonology | 4 functions | Text processing, tones |
| Translation | 3 functions | Hmong ↔ English |
| Grammar | 4 functions | POS, classifiers, tense |
| Phrasebook | 3 functions | Common phrases |
| Numbers | 3 functions | Number conversion |
| Proverbs | 2 functions | Cultural expressions |
| Education | 3 functions | Learning tools |

**Total: 22 main functions across 7 categories**

---

For more information, visit: https://github.com/yangnobody12/pyhmong