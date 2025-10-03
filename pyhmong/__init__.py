"""
PyHmong - Minimal Working Version
==================================

A professional Python library for Hmong language processing.
This is a minimal version with all 7 feature categories implemented.

Author: YangNobody12
Version: 0.1.0
License: MIT
"""

__version__ = '0.1.0'
__author__ = 'YangNobody12'
__email__ = 'yangnobody12@example.com'
__license__ = 'MIT'

import re
from typing import List, Dict, Optional, Tuple, Union
import random


# =============================================================================
# 1. PHONOLOGY & ORTHOGRAPHY
# =============================================================================

def normalize_text(text: str) -> str:
    """Normalize Hmong text (fix spacing, case, tones)."""
    # Remove extra spaces
    cleaned = ' '.join(text.split())
    
    # Capitalize first letter of sentences
    if cleaned:
        words = cleaned.split()
        words[0] = words[0].capitalize()
        words[1:] = [w.lower() for w in words[1:]]
        return ' '.join(words)
    return cleaned


def syllable_split(word: str) -> List[str]:
    """Split word into syllables."""
    return word.split()


def get_tone(syllable: str) -> str:
    """Get tone marker of syllable."""
    if syllable and syllable[-1].lower() in ['b', 'j', 'v', 's', 'g', 'd', 'm']:
        return syllable[-1].upper()
    return "NONE"


def convert_tone(syllable: str, target_tone: str) -> str:
    """Convert syllable to different tone."""
    # Remove current tone
    base = syllable.rstrip('bjvsgdmBJVSGDM')
    # Add new tone
    return base + target_tone.lower() if target_tone else base


# =============================================================================
# 2. DICTIONARY & TRANSLATION
# =============================================================================

_DICTIONARY_HM_TO_EN = {
    # Pronouns
    'kuv': 'I, me',
    'koj': 'you (singular)',
    'nws': 'he, she, it',
    'peb': 'we, us, three',
    'nej': 'you (plural)',
    'lawv': 'they, them',
    
    # Common verbs
    'yog': 'to be, is, am, are',
    'tsis': 'no, not',
    'nyob': 'to live, to stay, to be at',
    'zoo': 'good, well',
    'los': 'to come',
    'mus': 'to go',
    'ua': 'to do, to make',
    'tau': 'to get, to obtain, can',
    'yuav': 'will, want, going to',
    'xav': 'to think, to want',
    'paub': 'to know',
    'pom': 'to see',
    'noj': 'to eat',
    'haus': 'to drink',
    'pw': 'to sleep',
    'hais': 'to say, to speak',
    
    # Family
    'niam': 'mother',
    'txiv': 'father',
    'tub': 'son',
    'ntxhais': 'daughter',
    'kwv': 'younger brother',
    'tij': 'older brother',
    'muam': 'younger sister',
    
    # Food
    'mov': 'rice',
    'nqaij': 'meat',
    'zaub': 'vegetables',
    'kua': 'soup',
    'qe': 'egg',
    
    # Numbers
    'ib': 'one',
    'ob': 'two',
    'plaub': 'four',
    'tsib': 'five',
    'rau': 'six',
    'xya': 'seven',
    'yim': 'eight',
    'cuaj': 'nine',
    'kaum': 'ten',
    
    # Common words
    'neeg': 'person, people',
    'hmoob': 'Hmong',
    'tsev': 'house, home',
    'chaw': 'place',
    'lub': 'classifier',
    'tus': 'classifier',
    'hnub': 'day, sun',
    'hmo': 'night',
}

# Build reverse dictionary
_DICTIONARY_EN_TO_HM = {}
for hm, en in _DICTIONARY_HM_TO_EN.items():
    translations = [t.strip() for t in en.split(',')]
    for trans in translations:
        if trans not in _DICTIONARY_EN_TO_HM:
            _DICTIONARY_EN_TO_HM[trans] = []
        _DICTIONARY_EN_TO_HM[trans].append(hm)


def translate_hm_to_en(word: str) -> str:
    """Translate Hmong word to English."""
    return _DICTIONARY_HM_TO_EN.get(word.lower(), f"Translation not found for '{word}'")


def translate_en_to_hm(word: str) -> Union[str, List[str]]:
    """Translate English word to Hmong."""
    result = _DICTIONARY_EN_TO_HM.get(word.lower())
    if result:
        return result[0] if len(result) == 1 else result
    return f"Translation not found for '{word}'"


def search_dictionary(query: str, lang: str = "hm") -> List[Dict[str, str]]:
    """Search dictionary with fuzzy matching."""
    results = []
    query_lower = query.lower()
    
    if lang == "hm":
        for hm_word, en_trans in _DICTIONARY_HM_TO_EN.items():
            if query_lower in hm_word.lower():
                results.append({"hmong": hm_word, "english": en_trans})
    else:
        for en_word, hm_words in _DICTIONARY_EN_TO_HM.items():
            if query_lower in en_word.lower():
                for hm in hm_words:
                    results.append({"english": en_word, "hmong": hm})
    
    return results[:10]


# =============================================================================
# 3. GRAMMAR
# =============================================================================

_POS_DICT = {
    'kuv': 'pronoun', 'koj': 'pronoun', 'nws': 'pronoun',
    'peb': 'pronoun', 'nej': 'pronoun', 'lawv': 'pronoun',
    'tus': 'classifier', 'lub': 'classifier', 'txoj': 'classifier',
    'yog': 'verb', 'nyob': 'verb', 'mus': 'verb', 'los': 'verb',
    'neeg': 'noun', 'tsev': 'noun', 'hmoob': 'noun',
}

_CLASSIFIERS = {
    'neeg': ['tus'], 'tsev': ['lub'], 'tsheb': ['lub'],
    'kev': ['txoj'], 'ntawv': ['daim'], 'dev': ['tus'],
}


def detect_pos(word: str) -> str:
    """Detect part of speech."""
    return _POS_DICT.get(word.lower(), 'unknown')


def get_classifiers(noun: str) -> List[str]:
    """Get appropriate classifiers for a noun."""
    return _CLASSIFIERS.get(noun.lower(), ['tus'])


def conjugate(sentence: str, tense: str = "past") -> str:
    """Add tense markers to sentence."""
    if tense == "past":
        return f"{sentence} lawm"
    elif tense == "future":
        return f"yuav {sentence}"
    return sentence


def substitute(sentence: str, target: str, replacement: str) -> str:
    """Substitute words in sentence."""
    words = sentence.split()
    new_words = [replacement if w == target else w for w in words]
    return ' '.join(new_words)


# =============================================================================
# 4. PHRASEBOOK UTILITIES
# =============================================================================

_GREETINGS = {
    "morning": "Nyob zoo sawv ntxov",
    "afternoon": "Nyob zoo tav su",
    "evening": "Nyob zoo tsaus ntuj",
    "general": "Nyob zoo",
    "goodbye": "Sib ntsib dua",
}

_QUESTIONS = {
    "name": "Koj lub npe hu li cas?",
    "age": "Koj muaj pes tsawg xyoos?",
    "from": "Koj tuaj qhov twg los?",
    "doing": "Koj ua dab tsi?",
    "feeling": "Koj nyob li cas?",
    "where": "Koj nyob qhov twg?",
}

_DIALOGUES = {
    1: [
        ("Nyob zoo!", "Hello!"),
        ("Koj lub npe hu li cas?", "What is your name?"),
        ("Kuv lub npe hu ua Maiv.", "My name is Mai."),
    ],
    2: [
        ("Koj puas tshaib plab?", "Are you hungry?"),
        ("Kuv tshaib plab heev.", "I am very hungry."),
        ("Koj xav noj dab tsi?", "What do you want to eat?"),
    ],
}


def get_greeting(time: str = "general") -> str:
    """Get appropriate greeting."""
    return _GREETINGS.get(time, _GREETINGS["general"])


def ask_question(topic: str) -> str:
    """Get question phrase for topic."""
    return _QUESTIONS.get(topic, "Koj nyob li cas?")


def basic_dialogue(unit: int) -> List[Tuple[str, str]]:
    """Get dialogue for unit."""
    return _DIALOGUES.get(unit, [])


# =============================================================================
# 5. NUMBERS & MEASURES
# =============================================================================

_NUM_WORDS = {
    0: 'xoom', 1: 'ib', 2: 'ob', 3: 'peb', 4: 'plaub',
    5: 'tsib', 6: 'rau', 7: 'xya', 8: 'yim', 9: 'cuaj', 10: 'kaum',
}

_WORD_NUMS = {v: k for k, v in _NUM_WORDS.items()}


def num_to_hmong(n: int) -> str:
    """Convert number to Hmong words."""
    if n < 0 or n > 999999999:
        return str(n)

    if n in _NUM_WORDS:
        return _NUM_WORDS[n]

    if n < 20:
        return f"kaum {_NUM_WORDS[n - 10]}"

    if n < 100:
        tens, ones = n // 10, n % 10
        result = f"{_NUM_WORDS[tens]} caug"
        if ones > 0:
            result += f" {_NUM_WORDS[ones]}"
        return result

    parts = []

    # Millions
    if n >= 1000000:
        millions = n // 1000000
        if millions == 1:
            parts.append("ib lab")
        else:
            parts.append(f"{_convert_below_1000(millions)} lab")
        n %= 1000000

    # Thousands
    if n >= 1000:
        thousands = n // 1000
        if thousands == 1:
            parts.append("ib txhiab")
        else:
            parts.append(f"{_convert_below_1000(thousands)} txhiab")
        n %= 1000

    # Remaining hundreds, tens, ones
    if n > 0:
        parts.append(_convert_below_1000(n))

    return " ".join(parts)


def _convert_below_1000(n: int) -> str:
    """Helper to convert numbers below 1000 to Hmong text."""
    if n == 0:
        return ""
    if n in _NUM_WORDS:
        return _NUM_WORDS[n]

    parts = []

    # Hundreds
    if n >= 100:
        parts.append(f"{_NUM_WORDS[n // 100]} puas")
        n %= 100

    # Tens and ones
    if n >= 20:
        parts.append(f"{_NUM_WORDS[n // 10]} caug")
        n %= 10
        if n > 0:
            parts.append(_NUM_WORDS[n])
    elif n >= 11:
        parts.append(f"kaum {_NUM_WORDS[n - 10]}")
    elif n == 10:
        parts.append("kaum")
    elif n > 0:
        parts.append(_NUM_WORDS[n])

    return " ".join(parts)


def hmong_to_num(word: str) -> Optional[int]:
    """Convert Hmong words to number."""
    word = word.lower().strip()
    if word in _WORD_NUMS:
        return _WORD_NUMS[word]
    if 'kaum' in word:
        parts = word.split()
        if len(parts) == 2 and parts[0] == 'kaum':
            return 10 + _WORD_NUMS.get(parts[1], 0)
    return None


def convert_measure(value: float, from_unit: str, to_unit: str) -> str:
    """Convert between measurement units."""
    conversions = {
        ('lbs', 'kg'): 0.453592,
        ('kg', 'lbs'): 2.20462,
        ('miles', 'km'): 1.60934,
        ('km', 'miles'): 0.621371,
    }
    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        converted = value * conversions[key]
        return f"{value} {from_unit} = {converted:.2f} {to_unit}"
    return f"Conversion from {from_unit} to {to_unit} not available"


# =============================================================================
# 6. PROVERBS & IDIOMS
# =============================================================================

_PROVERBS = {
    "wisdom": ["Niam txiv lus yog lus qhuab qhia"],
    "family": ["Niam txiv siab zoo, me nyuam thiaj li zoo"],
    "work": ["Ua haujlwm tsis txhob so, noj mov thiaj li tsis tshaib"],
}

_IDIOMS = {
    "zoo siab": "happy (lit: good heart)",
    "siab phem": "mean, evil (lit: bad heart)",
    "siab ntev": "patient (lit: long heart)",
}


def get_proverb(topic: str = "wisdom") -> str:
    """Get a proverb by topic."""
    proverbs = _PROVERBS.get(topic, _PROVERBS["wisdom"])
    return random.choice(proverbs) if proverbs else ""


def explain_idiom(phrase: str) -> str:
    """Explain an idiom's meaning."""
    return _IDIOMS.get(phrase.lower(), f"Idiom '{phrase}' not found")


# =============================================================================
# 7. EDUCATION TOOLS
# =============================================================================

_FLASHCARDS = {
    "food": {"mov": "rice", "nqaij": "meat", "zaub": "vegetables"},
    "family": {"niam": "mother", "txiv": "father", "tub": "son"},
    "colors": {"dawb": "white", "dub": "black", "liab": "red"},
}


def generate_drill(drill_type: str = "tone") -> List[str]:
    """Generate pronunciation drill."""
    if drill_type == "tone":
        return ['pab', 'paj', 'pav', 'pas', 'pag', 'pad', 'pam', 'pa']
    elif drill_type == "consonant":
        return ['peb', 'keb', 'teb', 'neb', 'meb']
    elif drill_type == "vowel":
        return ['pa', 'pe', 'pi', 'po', 'pu']
    return []


def quiz_flashcards(category: str = "food") -> Dict[str, str]:
    """Get flashcard set for quiz."""
    return _FLASHCARDS.get(category, {})


def check_pronunciation(word: str) -> Dict[str, Union[str, bool]]:
    """Check word pronunciation structure."""
    tone = get_tone(word)
    is_valid = len(word) > 0
    
    return {
        "word": word,
        "valid": is_valid,
        "onset": word[0] if word else None,
        "nucleus": word[1:-1] if len(word) > 2 else word[1:],
        "tone": tone,
        "feedback": "Valid Hmong syllable" if is_valid else "Invalid structure"
    }


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def tokenize(text: str) -> List[str]:
    """Tokenize Hmong text into words."""
    return text.strip().split()


def is_valid_syllable(syllable: str) -> bool:
    """Check if syllable is valid Hmong."""
    if not syllable or not syllable.isalpha():
        return False

    # Valid Hmong vowels
    hmong_vowels = ['a', 'e', 'i', 'o', 'u', 'w', 'aa', 'ai', 'au', 'aw', 'ee', 'ia', 'oo', 'ua', 'aws']
    syllable_lower = syllable.lower()

    # Check if syllable contains at least one valid Hmong vowel
    has_vowel = any(vowel in syllable_lower for vowel in hmong_vowels)

    return has_vowel


def decompose_syllable(syllable: str) -> Dict[str, Optional[str]]:
    """Decompose syllable into onset, nucleus, coda."""
    if not syllable:
        return {'onset': None, 'nucleus': None, 'coda': None}
    
    tone_marker = syllable[-1] if syllable[-1].lower() in 'bjvsgdm' else None
    base = syllable[:-1] if tone_marker else syllable
    
    return {
        'onset': base[0] if base else None,
        'nucleus': base[1:] if len(base) > 1 else base,
        'coda': tone_marker
    }


def count_syllables(text: str) -> int:
    """Count syllables in text."""
    return len(tokenize(text))


# =============================================================================
# EXPORTS
# =============================================================================

__all__ = [
    # Version info
    '__version__', '__author__', '__email__', '__license__',
    
    # Phonology
    'normalize_text', 'syllable_split', 'get_tone', 'convert_tone',
    
    # Translation
    'translate_hm_to_en', 'translate_en_to_hm', 'search_dictionary',
    
    # Grammar
    'detect_pos', 'get_classifiers', 'conjugate', 'substitute',
    
    # Phrasebook
    'get_greeting', 'ask_question', 'basic_dialogue',
    
    # Numbers
    'num_to_hmong', 'hmong_to_num', 'convert_measure',
    
    # Proverbs
    'get_proverb', 'explain_idiom',
    
    # Education
    'generate_drill', 'quiz_flashcards', 'check_pronunciation',
    
    # Utilities
    'tokenize', 'is_valid_syllable', 'decompose_syllable', 'count_syllables',
]