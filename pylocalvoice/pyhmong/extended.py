"""
Extended Hmong Language Processing Features
============================================

This module extends the core functionality with:
1. Advanced phonology and orthography
2. Dictionary and translation
3. Grammar analysis
4. Phrasebook utilities
5. Numbers and measures
6. Proverbs and idioms
7. Education tools
"""

from typing import List, Dict, Optional, Tuple, Union
import random
from pyhmong.core import HmongProcessor, ToneMarker, PartOfSpeech


# ============================================================================
# 2. DICTIONARY & TRANSLATION
# ============================================================================

class HmongTranslator:
    """Hmong-English translation engine."""
    
    def __init__(self):
        """Initialize translator with dictionaries."""
        # Extended Hmong-English dictionary (based on Heimbach)
        self.hm_to_en = {
            # Pronouns
            'kuv': 'I, me',
            'koj': 'you (singular)',
            'nws': 'he, she, it',
            'peb': 'we, us',
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
            'niam': 'older sister',
            
            # Food
            'mov': 'rice',
            'nqaij': 'meat',
            'zaub': 'vegetables',
            'kua': 'soup',
            'qe': 'egg',
            
            # Body parts
            'taub hau': 'head',
            'qhov muag': 'eye',
            'qhov ntswg': 'nose',
            'qhov ncauj': 'mouth',
            'pob ntseg': 'ear',
            'tes': 'hand',
            'taw': 'foot',
            
            # Numbers
            'ib': 'one',
            'ob': 'two',
            'peb': 'three',
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
            'ntuj': 'sky',
            'av': 'earth, ground',
            'dej': 'water',
        }
        
        # Reverse dictionary for English to Hmong
        self.en_to_hm = {}
        for hm, en in self.hm_to_en.items():
            # Handle multiple translations
            translations = [t.strip() for t in en.split(',')]
            for trans in translations:
                if trans not in self.en_to_hm:
                    self.en_to_hm[trans] = []
                self.en_to_hm[trans].append(hm)
    
    def translate_hm_to_en(self, word: str) -> str:
        """
        Translate Hmong word to English.
        
        Args:
            word: Hmong word
            
        Returns:
            English translation or "Translation not found"
        """
        return self.hm_to_en.get(word.lower(), f"Translation not found for '{word}'")
    
    def translate_en_to_hm(self, word: str) -> Union[str, List[str]]:
        """
        Translate English word to Hmong.
        
        Args:
            word: English word
            
        Returns:
            Hmong translation(s) or error message
        """
        result = self.en_to_hm.get(word.lower())
        if result:
            return result[0] if len(result) == 1 else result
        return f"Translation not found for '{word}'"
    
    def search_dictionary(self, query: str, lang: str = "hm") -> List[Dict[str, str]]:
        """
        Search dictionary with fuzzy matching.
        
        Args:
            query: Search query
            lang: "hm" for Hmong or "en" for English
            
        Returns:
            List of matching entries
        """
        results = []
        query_lower = query.lower()
        
        if lang == "hm":
            for hm_word, en_trans in self.hm_to_en.items():
                if query_lower in hm_word.lower():
                    results.append({"hmong": hm_word, "english": en_trans})
        else:  # English
            for en_word, hm_words in self.en_to_hm.items():
                if query_lower in en_word.lower():
                    for hm in hm_words:
                        results.append({"english": en_word, "hmong": hm})
        
        return results[:10]  # Limit to 10 results


# ============================================================================
# 3. GRAMMAR
# ============================================================================

class HmongGrammar:
    """Hmong grammar analyzer and utilities."""
    
    def __init__(self):
        """Initialize grammar analyzer."""
        self.pos_dict = {
            # Pronouns
            'kuv': PartOfSpeech.PRONOUN,
            'koj': PartOfSpeech.PRONOUN,
            'nws': PartOfSpeech.PRONOUN,
            'peb': PartOfSpeech.PRONOUN,
            'nej': PartOfSpeech.PRONOUN,
            'lawv': PartOfSpeech.PRONOUN,
            
            # Classifiers
            'tus': PartOfSpeech.CLASSIFIER,
            'lub': PartOfSpeech.CLASSIFIER,
            'txoj': PartOfSpeech.CLASSIFIER,
            'daim': PartOfSpeech.CLASSIFIER,
            
            # Verbs
            'yog': PartOfSpeech.VERB,
            'nyob': PartOfSpeech.VERB,
            'mus': PartOfSpeech.VERB,
            'los': PartOfSpeech.VERB,
            'ua': PartOfSpeech.VERB,
            'tau': PartOfSpeech.VERB,
            
            # Nouns
            'neeg': PartOfSpeech.NOUN,
            'tsev': PartOfSpeech.NOUN,
            'hmoob': PartOfSpeech.NOUN,
        }
        
        # Classifiers for specific nouns
        self.classifiers = {
            'neeg': ['tus'],  # person
            'tsev': ['lub'],  # house
            'tsheb': ['lub'],  # car
            'kev': ['txoj'],  # road, way
            'ntawv': ['daim'],  # paper
            'dev': ['tus'],  # dog
            'miv': ['tus'],  # cat
        }
    
    def detect_pos(self, word: str) -> PartOfSpeech:
        """
        Detect part of speech for a word.
        
        Args:
            word: Hmong word
            
        Returns:
            PartOfSpeech enum
        """
        return self.pos_dict.get(word.lower(), PartOfSpeech.UNKNOWN)
    
    def get_classifiers(self, noun: str) -> List[str]:
        """
        Get appropriate classifiers for a noun.
        
        Args:
            noun: Hmong noun
            
        Returns:
            List of classifiers
        """
        return self.classifiers.get(noun.lower(), ['tus'])  # Default to 'tus'
    
    def conjugate(self, sentence: str, tense: str = "past") -> str:
        """
        Add tense markers to sentence.
        
        Args:
            sentence: Input sentence
            tense: "past", "future", or "present"
            
        Returns:
            Conjugated sentence
        """
        if tense == "past":
            return f"{sentence} lawm"  # completed action marker
        elif tense == "future":
            return f"yuav {sentence}"  # future marker
        return sentence  # present (no marker needed)
    
    def substitute(self, sentence: str, target: str, replacement: str) -> str:
        """
        Substitute words in sentence (grammar drill).
        
        Args:
            sentence: Original sentence
            target: Word to replace
            replacement: New word
            
        Returns:
            Modified sentence
        """
        words = sentence.split()
        new_words = [replacement if w == target else w for w in words]
        return ' '.join(new_words)


# ============================================================================
# 4. PHRASEBOOK UTILITIES
# ============================================================================

class HmongPhrasebook:
    """Common phrases and dialogues."""
    
    def __init__(self):
        """Initialize phrasebook."""
        self.greetings = {
            "morning": "Nyob zoo sawv ntxov",
            "afternoon": "Nyob zoo tav su",
            "evening": "Nyob zoo tsaus ntuj",
            "general": "Nyob zoo",
            "goodbye": "Sib ntsib dua",
        }
        
        self.questions = {
            "name": "Koj lub npe hu li cas?",
            "age": "Koj muaj pes tsawg xyoos?",
            "from": "Koj tuaj qhov twg los?",
            "doing": "Koj ua dab tsi?",
            "feeling": "Koj nyob li cas?",
            "where": "Koj nyob qhov twg?",
        }
        
        self.dialogues = {
            1: [  # Unit 1: Introductions
                ("Nyob zoo!", "Hello!"),
                ("Koj lub npe hu li cas?", "What is your name?"),
                ("Kuv lub npe hu ua Maiv.", "My name is Mai."),
                ("Zoo siab tau ntsib koj.", "Nice to meet you."),
            ],
            2: [  # Unit 2: Food
                ("Koj puas tshaib plab?", "Are you hungry?"),
                ("Kuv tshaib plab heev.", "I am very hungry."),
                ("Koj xav noj dab tsi?", "What do you want to eat?"),
                ("Kuv xav noj mov.", "I want to eat rice."),
            ],
            3: [  # Unit 3: Family
                ("Koj muaj pes tsawg tus me nyuam?", "How many children do you have?"),
                ("Kuv muaj ob tus tub.", "I have two sons."),
                ("Koj niam nyob qhov twg?", "Where does your mother live?"),
                ("Nws nyob hauv Nplog teb.", "She lives in Laos."),
            ],
        }
    
    def get_greeting(self, time: str = "general") -> str:
        """
        Get appropriate greeting.
        
        Args:
            time: "morning", "afternoon", "evening", or "general"
            
        Returns:
            Greeting phrase
        """
        return self.greetings.get(time, self.greetings["general"])
    
    def ask_question(self, topic: str) -> str:
        """
        Get question phrase for topic.
        
        Args:
            topic: Question topic
            
        Returns:
            Question phrase
        """
        return self.questions.get(topic, "Koj nyob li cas?")
    
    def basic_dialogue(self, unit: int) -> List[Tuple[str, str]]:
        """
        Get dialogue for unit.
        
        Args:
            unit: Unit number (1-3)
            
        Returns:
            List of (Hmong, English) tuples
        """
        return self.dialogues.get(unit, [])


# ============================================================================
# 5. NUMBERS & MEASURES
# ============================================================================

class HmongNumbers:
    """Number and measurement conversions."""
    
    def __init__(self):
        """Initialize number system."""
        self.num_words = {
            0: 'xoom',
            1: 'ib',
            2: 'ob',
            3: 'peb',
            4: 'plaub',
            5: 'tsib',
            6: 'rau',
            7: 'xya',
            8: 'yim',
            9: 'cuaj',
            10: 'kaum',
            100: 'pua',
            1000: 'txhiab',
        }
        
        # Reverse mapping
        self.word_nums = {v: k for k, v in self.num_words.items()}
    
    def num_to_hmong(self, n: int) -> str:
        """
        Convert number to Hmong words.
        
        Args:
            n: Integer number
            
        Returns:
            Hmong number words
        """
        if n in self.num_words:
            return self.num_words[n]
        
        if n < 20:
            return f"kaum {self.num_words[n - 10]}"
        
        if n < 100:
            tens = n // 10
            ones = n % 10
            if ones == 0:
                return f"{self.num_words[tens]} kaum"
            return f"{self.num_words[tens]} kaum {self.num_words[ones]}"
        
        if n < 1000:
            hundreds = n // 100
            remainder = n % 100
            result = f"{self.num_words[hundreds]} pua"
            if remainder > 0:
                result += f" {self.num_to_hmong(remainder)}"
            return result
        
        return str(n)  # Fallback for large numbers
    
    def hmong_to_num(self, word: str) -> Optional[int]:
        """
        Convert Hmong words to number.
        
        Args:
            word: Hmong number word
            
        Returns:
            Integer or None
        """
        word = word.lower().strip()
        if word in self.word_nums:
            return self.word_nums[word]
        
        # Handle compound numbers
        if 'kaum' in word:
            parts = word.split()
            if len(parts) == 2 and parts[0] == 'kaum':
                return 10 + self.word_nums.get(parts[1], 0)
            elif len(parts) == 2 and parts[1] == 'kaum':
                return self.word_nums.get(parts[0], 0) * 10
            elif len(parts) == 3:
                tens = self.word_nums.get(parts[0], 0) * 10
                ones = self.word_nums.get(parts[2], 0)
                return tens + ones
        
        return None


# ============================================================================
# 6. PROVERBS & IDIOMS
# ============================================================================

class HmongProverbs:
    """Hmong proverbs and idioms."""
    
    def __init__(self):
        """Initialize proverb database."""
        self.proverbs = {
            "wisdom": [
                "Niam txiv lus yog lus qhuab qhia",
                "Ib tug xibfwb qhia ntau tus tub kawm",
            ],
            "family": [
                "Niam txiv siab zoo, me nyuam thiaj li zoo",
                "Kwv tij sib hlub, yeeb ncuab thiaj li ntshai",
            ],
            "work": [
                "Ua haujlwm tsis txhob so, noj mov thiaj li tsis tshaib",
            ],
        }
        
        self.idioms = {
            "zoo siab": "happy (lit: good heart)",
            "siab phem": "mean, evil (lit: bad heart)",
            "siab ntev": "patient (lit: long heart)",
        }
    
    def get_proverb(self, topic: str = "wisdom") -> str:
        """
        Get a proverb by topic.
        
        Args:
            topic: Proverb category
            
        Returns:
            Hmong proverb
        """
        proverbs = self.proverbs.get(topic, self.proverbs["wisdom"])
        return random.choice(proverbs) if proverbs else ""
    
    def explain_idiom(self, phrase: str) -> str:
        """
        Explain an idiom's meaning.
        
        Args:
            phrase: Hmong idiom
            
        Returns:
            Explanation
        """
        return self.idioms.get(phrase.lower(), f"Idiom '{phrase}' not found")


# ============================================================================
# 7. EDUCATION TOOLS
# ============================================================================

class HmongEducation:
    """Educational tools and drills."""
    
    def __init__(self):
        """Initialize education tools."""
        self.processor = HmongProcessor()
        
        self.flashcards = {
            "food": {
                "mov": "rice",
                "nqaij": "meat",
                "zaub": "vegetables",
                "kua": "soup",
            },
            "family": {
                "niam": "mother",
                "txiv": "father",
                "tub": "son",
                "ntxhais": "daughter",
            },
            "colors": {
                "dawb": "white",
                "dub": "black",
                "liab": "red",
                "ntsuab": "green",
            },
        }
    
    def generate_drill(self, drill_type: str = "tone") -> List[str]:
        """
        Generate pronunciation drills.
        
        Args:
            drill_type: "tone", "consonant", or "vowel"
            
        Returns:
            List of practice words
        """
        if drill_type == "tone":
            base = "pa"
            return [f"{base}{tone}" for tone in ['b', 'j', 'v', 's', 'g', 'd', 'm', '']]
        
        elif drill_type == "consonant":
            return ['peb', 'keb', 'teb', 'neb', 'meb']
        
        elif drill_type == "vowel":
            return ['pa', 'pe', 'pi', 'po', 'pu']
        
        return []
    
    def quiz_flashcards(self, category: str = "food") -> Dict[str, str]:
        """
        Get flashcard set for quiz.
        
        Args:
            category: Flashcard category
            
        Returns:
            Dictionary of Hmong-English pairs
        """
        return self.flashcards.get(category, {})
    
    def check_pronunciation(self, word: str) -> Dict[str, Union[str, bool]]:
        """
        Check pronunciation structure (placeholder for audio).
        
        Args:
            word: Word to check
            
        Returns:
            Analysis dictionary
        """
        is_valid = self.processor.is_valid_syllable(word)
        parts = self.processor.decompose_syllable(word)
        tone = self.processor.get_tone(word)
        
        return {
            "word": word,
            "valid": is_valid,
            "onset": parts['onset'],
            "nucleus": parts['nucleus'],
            "tone": tone.name if tone else "NONE",
            "feedback": "Valid Hmong syllable" if is_valid else "Invalid structure"
        }