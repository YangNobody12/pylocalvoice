# TODO: Copy content from artifact "Unit Tests"
"""
Unit tests for pyhmong library
"""

import unittest
from pyhmong import (
    HmongProcessor,
    HmongDictionary,
    RomanizationSystem,
    ToneMarker,
    tokenize,
    is_valid_syllable,
    normalize
)


class TestHmongProcessor(unittest.TestCase):
    """Test cases for HmongProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.processor = HmongProcessor()
    
    def test_tokenize_basic(self):
        """Test basic tokenization."""
        text = "Kuv yog neeg Hmoob"
        expected = ["Kuv", "yog", "neeg", "Hmoob"]
        self.assertEqual(self.processor.tokenize(text), expected)
    
    def test_tokenize_empty(self):
        """Test tokenization of empty string."""
        self.assertEqual(self.processor.tokenize(""), [])
    
    def test_tokenize_extra_spaces(self):
        """Test tokenization with extra spaces."""
        text = "Kuv   yog    neeg"
        expected = ["Kuv", "yog", "neeg"]
        self.assertEqual(self.processor.tokenize(text), expected)
    
    def test_is_valid_syllable_valid(self):
        """Test validation of valid syllables."""
        valid_syllables = ["kuv", "peb", "hmoob", "ntxawg", "nyob", "zoo"]
        for syllable in valid_syllables:
            with self.subTest(syllable=syllable):
                self.assertTrue(self.processor.is_valid_syllable(syllable))
    
    def test_is_valid_syllable_invalid(self):
        """Test validation of invalid syllables."""
        invalid_syllables = ["xyz", "bcd", "qqq"]
        for syllable in invalid_syllables:
            with self.subTest(syllable=syllable):
                self.assertFalse(self.processor.is_valid_syllable(syllable))
    
    def test_get_tone_with_marker(self):
        """Test tone extraction with tone marker."""
        test_cases = [
            ("kuv", ToneMarker.V),
            ("peb", ToneMarker.B),
            ("koj", ToneMarker.J),
            ("nws", ToneMarker.S),
        ]
        for syllable, expected_tone in test_cases:
            with self.subTest(syllable=syllable):
                self.assertEqual(self.processor.get_tone(syllable), expected_tone)
    
    def test_get_tone_no_marker(self):
        """Test tone extraction without tone marker."""
        self.assertEqual(self.processor.get_tone("ha"), ToneMarker.NONE)
    
    def test_decompose_syllable(self):
        """Test syllable decomposition."""
        test_cases = [
            ("kuv", {"onset": "k", "nucleus": "u", "coda": "v"}),
            ("ntxawg", {"onset": "ntx", "nucleus": "aw", "coda": "g"}),
            ("zoo", {"onset": "z", "nucleus": "oo", "coda": None}),
            ("ib", {"onset": None, "nucleus": "i", "coda": "b"}),
        ]
        for syllable, expected in test_cases:
            with self.subTest(syllable=syllable):
                self.assertEqual(self.processor.decompose_syllable(syllable), expected)
    
    def test_count_syllables(self):
        """Test syllable counting."""
        test_cases = [
            ("Kuv yog neeg Hmoob", 4),
            ("Nyob zoo", 2),
            ("", 0),
            ("Ib", 1),
        ]
        for text, expected_count in test_cases:
            with self.subTest(text=text):
                self.assertEqual(self.processor.count_syllables(text), expected_count)
    
    def test_normalize(self):
        """Test text normalization."""
        test_cases = [
            ("kuv   yog  neeg", "Kuv yog neeg"),
            ("KUVA YOG NEEG", "Kuva yog neeg"),
            ("  nyob  zoo  ", "Nyob zoo"),
        ]
        for text, expected in test_cases:
            with self.subTest(text=text):
                self.assertEqual(self.processor.normalize(text), expected)
    
    def test_get_initial_consonants(self):
        """Test getting initial consonants."""
        consonants = self.processor.get_initial_consonants()
        self.assertIsInstance(consonants, set)
        self.assertIn('k', consonants)
        self.assertIn('ntx', consonants)
        self.assertIn('ch', consonants)
    
    def test_get_vowels(self):
        """Test getting vowels."""
        vowels = self.processor.get_vowels()
        self.assertIsInstance(vowels, set)
        self.assertIn('a', vowels)
        self.assertIn('oo', vowels)
        self.assertIn('ai', vowels)


class TestHmongDictionary(unittest.TestCase):
    """Test cases for HmongDictionary class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.dictionary = HmongDictionary()
    
    def test_lookup_existing_word(self):
        """Test looking up existing words."""
        self.assertEqual(self.dictionary.lookup("kuv"), "I, me")
        self.assertEqual(self.dictionary.lookup("koj"), "you")
    
    def test_lookup_nonexisting_word(self):
        """Test looking up non-existing word."""
        self.assertIsNone(self.dictionary.lookup("xyz"))
    
    def test_lookup_case_insensitive(self):
        """Test that lookup is case-insensitive."""
        self.assertEqual(self.dictionary.lookup("KUV"), "I, me")
        self.assertEqual(self.dictionary.lookup("Kuv"), "I, me")
    
    def test_add_word(self):
        """Test adding new word."""
        self.dictionary.add_word("tsev", "house")
        self.assertEqual(self.dictionary.lookup("tsev"), "house")
    
    def test_get_all_words(self):
        """Test getting all words."""
        words = self.dictionary.get_all_words()
        self.assertIsInstance(words, list)
        self.assertIn("kuv", words)
        self.assertIn("koj", words)
        # Check that list is sorted
        self.assertEqual(words, sorted(words))


class TestConvenienceFunctions(unittest.TestCase):
    """Test cases for convenience functions."""
    
    def test_tokenize_function(self):
        """Test tokenize convenience function."""
        result = tokenize("Kuv yog neeg")
        self.assertEqual(result, ["Kuv", "yog", "neeg"])
    
    def test_is_valid_syllable_function(self):
        """Test is_valid_syllable convenience function."""
        self.assertTrue(is_valid_syllable("kuv"))
        self.assertFalse(is_valid_syllable("xyz"))
    
    def test_normalize_function(self):
        """Test normalize convenience function."""
        result = normalize("kuv  yog  neeg")
        self.assertEqual(result, "Kuv yog neeg")


class TestEnums(unittest.TestCase):
    """Test cases for enum classes."""
    
    def test_romanization_system_enum(self):
        """Test RomanizationSystem enum."""
        self.assertEqual(RomanizationSystem.RPA.value, "Romanized Popular Alphabet")
        self.assertEqual(RomanizationSystem.PAHAWH.value, "Pahawh Hmong")
    
    def test_tone_marker_enum(self):
        """Test ToneMarker enum."""
        self.assertEqual(ToneMarker.B.value, "mid-low tone")
        self.assertEqual(ToneMarker.V.value, "mid-high rising tone")
        self.assertEqual(ToneMarker.NONE.value, "mid tone (unmarked)")


if __name__ == '__main__':
    unittest.main()