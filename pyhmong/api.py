"""
PyHmong Complete API
====================

Convenience functions for all features
"""

from pyhmong.core import HmongProcessor
from pyhmong.extended import (
    HmongTranslator,
    HmongGrammar,
    HmongPhrasebook,
    HmongNumbers,
    HmongProverbs,
    HmongEducation
)
from typing import List, Dict, Optional, Tuple, Union


# Initialize all components
_processor = HmongProcessor()
_translator = HmongTranslator()
_grammar = HmongGrammar()
_phrasebook = HmongPhrasebook()
_numbers = HmongNumbers()
_proverbs = HmongProverbs()
_education = HmongEducation()


# ============================================================================
# 1. PHONOLOGY & ORTHOGRAPHY
# ============================================================================

def normalize_text(text: str) -> str:
    """Normalize Hmong text (spacing, case, tones)."""
    return _processor.normalize_text(text)


def syllable_split(word: str) -> List[str]:
    """Split word into syllables."""
    return _processor.syllable_split(word)


def get_tone(syllable: str) -> str:
    """Get tone marker of syllable."""
    tone = _processor.get_tone(syllable)
    return tone.name if tone else "NONE"


def convert_tone(syllable: str, target_tone: str) -> str:
    """Convert syllable to different tone."""
    return _processor.convert_tone(syllable, target_tone)


# ============================================================================
# 2. DICTIONARY & TRANSLATION
# ============================================================================

def translate_hm_to_en(word: str) -> str:
    """Translate Hmong word to English."""
    return _translator.translate_hm_to_en(word)


def translate_en_to_hm(word: str) -> Union[str, List[str]]:
    """Translate English word to Hmong."""
    return _translator.translate_en_to_hm(word)


def search_dictionary(query: str, lang: str = "hm") -> List[Dict[str, str]]:
    """Search dictionary for matches."""
    return _translator.search_dictionary(query, lang)


# ============================================================================
# 3. GRAMMAR
# ============================================================================

def detect_pos(word: str) -> str:
    """Detect part of speech."""
    pos = _grammar.detect_pos(word)
    return pos.value


def get_classifiers(noun: str) -> List[str]:
    """Get classifiers for a noun."""
    return _grammar.get_classifiers(noun)


def conjugate(sentence: str, tense: str = "past") -> str:
    """Conjugate sentence for tense."""
    return _grammar.conjugate(sentence, tense)


def substitute(sentence: str, target: str, replacement: str) -> str:
    """Substitute word in sentence."""
    return _grammar.substitute(sentence, target, replacement)


# ============================================================================
# 4. PHRASEBOOK UTILITIES
# ============================================================================

def get_greeting(time: str = "general") -> str:
    """Get appropriate greeting."""
    return _phrasebook.get_greeting(time)


def ask_question(topic: str) -> str:
    """Get question phrase for topic."""
    return _phrasebook.ask_question(topic)


def basic_dialogue(unit: int) -> List[Tuple[str, str]]:
    """Get basic dialogue by unit."""
    return _phrasebook.basic_dialogue(unit)


# ============================================================================
# 5. NUMBERS & MEASURES
# ============================================================================

def num_to_hmong(n: int) -> str:
    """Convert number to Hmong words."""
    return _numbers.num_to_hmong(n)


def hmong_to_num(word: str) -> Optional[int]:
    """Convert Hmong words to number."""
    return _numbers.hmong_to_num(word)


def convert_measure(value: float, from_unit: str, to_unit: str) -> str:
    """
    Convert between measurement units.
    
    Args:
        value: Numeric value
        from_unit: Source unit (e.g., 'lbs', 'kg')
        to_unit: Target unit
        
    Returns:
        Converted value with explanation
        
    Example:
        >>> convert_measure(10, 'lbs', 'kg')
        '10 lbs = 4.54 kg'
    """
    conversions = {
        ('lbs', 'kg'): 0.453592,
        ('kg', 'lbs'): 2.20462,
        ('miles', 'km'): 1.60934,
        ('km', 'miles'): 0.621371,
        ('feet', 'meters'): 0.3048,
        ('meters', 'feet'): 3.28084,
    }
    
    key = (from_unit.lower(), to_unit.lower())
    if key in conversions:
        converted = value * conversions[key]
        return f"{value} {from_unit} = {converted:.2f} {to_unit}"
    
    return f"Conversion from {from_unit} to {to_unit} not available"


# ============================================================================
# 6. PROVERBS & IDIOMS
# ============================================================================

def get_proverb(topic: str = "wisdom") -> str:
    """Get a Hmong proverb by topic."""
    return _proverbs.get_proverb(topic)


def explain_idiom(phrase: str) -> str:
    """Explain idiom meaning."""
    return _proverbs.explain_idiom(phrase)


# ============================================================================
# 7. EDUCATION TOOLS
# ============================================================================

def generate_drill(drill_type: str = "tone") -> List[str]:
    """Generate pronunciation drill."""
    return _education.generate_drill(drill_type)


def quiz_flashcards(category: str = "food") -> Dict[str, str]:
    """Get flashcard quiz by category."""
    return _education.quiz_flashcards(category)


def check_pronunciation(word: str) -> Dict[str, Union[str, bool]]:
    """Check word pronunciation structure."""
    return _education.check_pronunciation(word)


# ============================================================================
# ADDITIONAL UTILITIES
# ============================================================================

def tokenize(text: str) -> List[str]:
    """Tokenize Hmong text into words."""
    return _processor.tokenize(text)


def is_valid_syllable(syllable: str) -> bool:
    """Check if syllable is valid Hmong."""
    return _processor.is_valid_syllable(syllable)


def decompose_syllable(syllable: str) -> Dict[str, Optional[str]]:
    """Decompose syllable into onset, nucleus, coda."""
    return _processor.decompose_syllable(syllable)


def count_syllables(text: str) -> int:
    """Count syllables in text."""
    return _processor.count_syllables(text)


# Export all functions
__all__ = [
    # Phonology
    'normalize_text',
    'syllable_split',
    'get_tone',
    'convert_tone',
    
    # Translation
    'translate_hm_to_en',
    'translate_en_to_hm',
    'search_dictionary',
    
    # Grammar
    'detect_pos',
    'get_classifiers',
    'conjugate',
    'substitute',
    
    # Phrasebook
    'get_greeting',
    'ask_question',
    'basic_dialogue',
    
    # Numbers
    'num_to_hmong',
    'hmong_to_num',
    'convert_measure',
    
    # Proverbs
    'get_proverb',
    'explain_idiom',
    
    # Education
    'generate_drill',
    'quiz_flashcards',
    'check_pronunciation',
    
    # Utilities
    'tokenize',
    'is_valid_syllable',
    'decompose_syllable',
    'count_syllables',
]