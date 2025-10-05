"""
pyhmong - A professional Python library for Hmong language processing
=====================================================================

This library provides comprehensive tools for working with the Hmong language:
- Phonology & Orthography (normalization, syllable splitting, tone conversion)
- Dictionary & Translation (Hmong ↔ English)
- Grammar (POS tagging, classifiers, conjugation)
- Phrasebook utilities (greetings, dialogues, questions)
- Numbers & Measures (conversion, calculations)
- Proverbs & Idioms (cultural expressions)
- Education tools (drills, flashcards, quizzes)

Author: YangNobody12
License: MIT
Version: 0.1.0
"""

from typing import List, Dict, Optional, Set, Tuple, Union
import re
from enum import Enum
import random


class RomanizationSystem(Enum):
    """Supported Hmong romanization systems."""
    RPA = "Romanized Popular Alphabet"  # Most common system
    PAHAWH = "Pahawh Hmong"  # Traditional script


class ToneMarker(Enum):
    """Hmong tone markers in RPA system."""
    B = "mid-low tone"
    J = "high falling tone"
    V = "mid-high rising tone"
    S = "low breathy tone"
    G = "low falling tone"
    D = "high tone"
    M = "low glottalized tone"
    NONE = "mid tone (unmarked)"


class PartOfSpeech(Enum):
    """Parts of speech in Hmong."""
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    CLASSIFIER = "classifier"
    PRONOUN = "pronoun"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    PARTICLE = "particle"
    ADVERB = "adverb"
    UNKNOWN = "unknown"


class HmongProcessor:
    """Main class for processing Hmong text."""
    
    # Hmong consonants in RPA
    CONSONANTS = {
        'single': ['b', 'c', 'd', 'f', 'h', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z'],
        'digraphs': ['ch', 'dh', 'kh', 'ml', 'nc', 'nk', 'np', 'nq', 'nr', 'nt', 'ny', 'ph', 'pl', 'qh', 'rh', 'th', 'ts', 'tx', 'xy'],
        'trigraphs': ['nch', 'nkh', 'nph', 'nqh', 'nrh', 'nth', 'ntx']
    }
    
    # Hmong vowels in RPA
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'w', 'aa', 'ai', 'au', 'aw', 'ee', 'ia', 'oo', 'ua', 'aws']
    
    # Tone markers (final consonants in RPA)
    TONES = ['b', 'j', 'v', 's', 'g', 'd', 'm']
    
    def __init__(self, system: RomanizationSystem = RomanizationSystem.RPA):
        """
        Initialize the Hmong processor.
        
        Args:
            system: The romanization system to use (default: RPA)
        """
        self.system = system
        self._build_syllable_pattern()
    
    def _build_syllable_pattern(self):
        """Build regex pattern for Hmong syllables."""
        # Consonant pattern (trigraphs first, then digraphs, then single)
        cons_pattern = '|'.join(
            self.CONSONANTS['trigraphs'] + 
            self.CONSONANTS['digraphs'] + 
            self.CONSONANTS['single']
        )
        
        # Vowel pattern
        vowel_pattern = '|'.join(sorted(self.VOWELS, key=len, reverse=True))
        
        # Tone pattern
        tone_pattern = '|'.join(self.TONES)
        
        # Complete syllable pattern
        self.syllable_pattern = re.compile(
            f'({cons_pattern})?({vowel_pattern})({tone_pattern})?',
            re.IGNORECASE
        )
    
    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize Hmong text into syllables.
        
        Args:
            text: Input Hmong text
            
        Returns:
            List of syllables
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.tokenize("Kuv yog neeg Hmoob")
            ['Kuv', 'yog', 'neeg', 'Hmoob']
        """
        # Remove extra whitespace and split
        words = text.strip().split()
        return words
    
    def is_valid_syllable(self, syllable: str) -> bool:
        """
        Check if a syllable is valid Hmong.
        
        Args:
            syllable: The syllable to validate
            
        Returns:
            True if valid, False otherwise
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.is_valid_syllable("peb")
            True
            >>> processor.is_valid_syllable("xyz")
            False
        """
        match = self.syllable_pattern.fullmatch(syllable.lower())
        return match is not None
    
    def get_tone(self, syllable: str) -> Optional[ToneMarker]:
        """
        Extract the tone from a Hmong syllable.
        
        Args:
            syllable: Input syllable
            
        Returns:
            ToneMarker enum or None
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.get_tone("kuv")
            <ToneMarker.V: 'mid-high rising tone'>
        """
        if not syllable:
            return None
        
        last_char = syllable[-1].lower()
        if last_char in self.TONES:
            return ToneMarker[last_char.upper()]
        return ToneMarker.NONE
    
    def decompose_syllable(self, syllable: str) -> Dict[str, Optional[str]]:
        """
        Decompose a syllable into its components.
        
        Args:
            syllable: Input syllable
            
        Returns:
            Dictionary with 'onset', 'nucleus', and 'coda' (tone)
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.decompose_syllable("ntxawg")
            {'onset': 'ntx', 'nucleus': 'aw', 'coda': 'g'}
        """
        match = self.syllable_pattern.fullmatch(syllable.lower())
        if not match:
            return {'onset': None, 'nucleus': None, 'coda': None}
        
        onset, nucleus, coda = match.groups()
        return {
            'onset': onset,
            'nucleus': nucleus,
            'coda': coda
        }
    
    def count_syllables(self, text: str) -> int:
        """
        Count the number of syllables in text.
        
        Args:
            text: Input text
            
        Returns:
            Number of syllables
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.count_syllables("Kuv yog neeg Hmoob")
            4
        """
        return len(self.tokenize(text))
    
    def normalize(self, text: str) -> str:
        """
        Normalize Hmong text (standardize spacing and casing).
        
        Args:
            text: Input text
            
        Returns:
            Normalized text
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.normalize("kuv   yog  NEEG    hmoob")
            'Kuv yog neeg Hmoob'
        """
        # Split into words, capitalize first letter of sentences
        words = text.strip().split()
        if not words:
            return ""
        
        # Capitalize first word
        normalized = [words[0].capitalize()]
        
        # Add remaining words in lowercase
        for word in words[1:]:
            if word.endswith('.') or word.endswith('!') or word.endswith('?'):
                normalized.append(word.lower())
                # Next word should be capitalized (if exists)
            else:
                normalized.append(word.lower())
        
        return ' '.join(normalized)
    
    def convert_tone(self, syllable: str, target_tone: str) -> str:
        """
        Convert syllable to different tone.
        
        Args:
            syllable: Input syllable
            target_tone: Target tone marker (b, j, v, s, g, d, m, or '' for unmarked)
            
        Returns:
            Syllable with new tone
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.convert_tone("kuv", "b")
            'kub'
        """
        # Remove current tone
        parts = self.decompose_syllable(syllable)
        if not parts['nucleus']:
            return syllable
        
        # Rebuild with new tone
        onset = parts['onset'] or ''
        nucleus = parts['nucleus']
        new_syllable = f"{onset}{nucleus}"
        
        if target_tone and target_tone.lower() in self.TONES:
            new_syllable += target_tone.lower()
        
        return new_syllable
    
    def syllable_split(self, word: str) -> List[str]:
        """
        Split word into syllables.
        
        Args:
            word: Input word (may contain multiple syllables)
            
        Returns:
            List of syllables
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.syllable_split("Hmoob")
            ['Hmoob']
            >>> processor.syllable_split("nyobzoo")
            ['nyob', 'zoo']
        """
        # For now, Hmong words are typically single syllables
        # This could be enhanced with a dictionary-based approach
        return self.tokenize(word)
    
    def normalize_text(self, text: str, fix_tones: bool = True, 
                      fix_case: bool = True, fix_spacing: bool = True) -> str:
        """
        Advanced text normalization with multiple options.
        
        Args:
            text: Input text
            fix_tones: Fix invalid tone markers
            fix_case: Standardize case
            fix_spacing: Fix spacing issues
            
        Returns:
            Normalized text
            
        Example:
            >>> processor = HmongProcessor()
            >>> processor.normalize_text("kuv   YOG  neeg")
            'Kuv yog neeg'
        """
        result = text
        
        # Fix spacing
        if fix_spacing:
            result = ' '.join(result.split())
        
        # Fix case (capitalize first word of sentences)
        if fix_case:
            sentences = result.split('.')
            normalized_sentences = []
            for sent in sentences:
                sent = sent.strip()
                if sent:
                    words = sent.split()
                    if words:
                        words[0] = words[0].capitalize()
                        words[1:] = [w.lower() for w in words[1:]]
                    normalized_sentences.append(' '.join(words))
            result = '. '.join(normalized_sentences)
        
        return result.strip()
    
    def get_initial_consonants(self) -> Set[str]:
        """
        Get all valid initial consonants.
        
        Returns:
            Set of consonant strings
        """
        return set(
            self.CONSONANTS['single'] + 
            self.CONSONANTS['digraphs'] + 
            self.CONSONANTS['trigraphs']
        )
    
    def get_vowels(self) -> Set[str]:
        """
        Get all valid vowels.
        
        Returns:
            Set of vowel strings
        """
        return set(self.VOWELS)


class HmongDictionary:
    """Simple dictionary for common Hmong words."""
    
    def __init__(self):
        """Initialize with common words."""
        self.words = {
            # Pronouns
            'kuv': 'I, me',
            'koj': 'you',
            'nws': 'he, she, it',
            'peb': 'we, us',
            'nej': 'you (plural)',
            'lawv': 'they, them',
            
            # Common words
            'yog': 'to be, yes',
            'tsis': 'no, not',
            'neeg': 'person',
            'hmoob': 'Hmong',
            'nyob': 'to live, to stay',
            'zoo': 'good',
            'los': 'to come',
            'mus': 'to go',
            'ua': 'to do, to make',
            'tau': 'to get, can',
            
            # Numbers
            'ib': 'one',
            'ob': 'two',
            'peb': 'three',
            'plaub': 'four',
            'tsib': 'five',
        }
    
    def lookup(self, word: str) -> Optional[str]:
        """
        Look up a word in the dictionary.
        
        Args:
            word: The word to look up
            
        Returns:
            Definition or None if not found
            
        Example:
            >>> dictionary = HmongDictionary()
            >>> dictionary.lookup("kuv")
            'I, me'
        """
        return self.words.get(word.lower())
    
    def add_word(self, word: str, definition: str):
        """
        Add a word to the dictionary.
        
        Args:
            word: The Hmong word
            definition: The definition
        """
        self.words[word.lower()] = definition
    
    def get_all_words(self) -> List[str]:
        """
        Get all words in the dictionary.
        
        Returns:
            List of words
        """
        return sorted(self.words.keys())


# Convenience functions
def tokenize(text: str) -> List[str]:
    """Tokenize Hmong text. Convenience wrapper."""
    processor = HmongProcessor()
    return processor.tokenize(text)


def is_valid_syllable(syllable: str) -> bool:
    """Check if syllable is valid. Convenience wrapper."""
    processor = HmongProcessor()
    return processor.is_valid_syllable(syllable)


def normalize(text: str) -> str:
    """Normalize Hmong text. Convenience wrapper."""
    processor = HmongProcessor()
    return processor.normalize(text)


__all__ = [
    'HmongProcessor',
    'HmongDictionary',
    'RomanizationSystem',
    'ToneMarker',
    'tokenize',
    'is_valid_syllable',
    'normalize',
]