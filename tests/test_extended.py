"""
Extended unit tests for all pyhmong features
"""

import unittest
import pyhmong


class TestPhonology(unittest.TestCase):
    """Test phonology and orthography features."""
    
    def test_normalize_text(self):
        """Test text normalization."""
        self.assertEqual(
            pyhmong.normalize_text("kuv  YOG  neeg"),
            "Kuv yog neeg"
        )
    
    def test_syllable_split(self):
        """Test syllable splitting."""
        result = pyhmong.syllable_split("Nyob zoo")
        self.assertEqual(len(result), 2)
    
    def test_get_tone(self):
        """Test tone detection."""
        self.assertEqual(pyhmong.get_tone("kuv"), "V")
        self.assertEqual(pyhmong.get_tone("zoo"), "NONE")
    
    def test_convert_tone(self):
        """Test tone conversion."""
        result = pyhmong.convert_tone("kuv", "b")
        self.assertEqual(result, "kub")


class TestTranslation(unittest.TestCase):
    """Test dictionary and translation features."""
    
    def test_translate_hm_to_en(self):
        """Test Hmong to English translation."""
        self.assertIn("mother", pyhmong.translate_hm_to_en("niam"))
    
    def test_translate_en_to_hm(self):
        """Test English to Hmong translation."""
        result = pyhmong.translate_en_to_hm("mother")
        self.assertIsInstance(result, (str, list))
    
    def test_search_dictionary(self):
        """Test dictionary search."""
        results = pyhmong.search_dictionary("kuv", lang="hm")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)


class TestGrammar(unittest.TestCase):
    """Test grammar features."""
    
    def test_detect_pos(self):
        """Test POS detection."""
        self.assertEqual(pyhmong.detect_pos("kuv"), "pronoun")
        self.assertEqual(pyhmong.detect_pos("yog"), "verb")
    
    def test_get_classifiers(self):
        """Test classifier retrieval."""
        classifiers = pyhmong.get_classifiers("neeg")
        self.assertIn("tus", classifiers)
    
    def test_conjugate(self):
        """Test conjugation."""
        sentence = "Kuv mus tsev"
        past = pyhmong.conjugate(sentence, "past")
        self.assertIn("lawm", past)
        
        future = pyhmong.conjugate(sentence, "future")
        self.assertIn("yuav", future)
    
    def test_substitute(self):
        """Test word substitution."""
        result = pyhmong.substitute("Kuv yog neeg", "Kuv", "Koj")
        self.assertEqual(result, "Koj yog neeg")


class TestPhrasebook(unittest.TestCase):
    """Test phrasebook features."""
    
    def test_get_greeting(self):
        """Test greeting retrieval."""
        self.assertIn("Nyob zoo", pyhmong.get_greeting("general"))
        self.assertIn("sawv ntxov", pyhmong.get_greeting("morning"))
    
    def test_ask_question(self):
        """Test question phrases."""
        question = pyhmong.ask_question("name")
        self.assertIn("npe", question)
    
    def test_basic_dialogue(self):
        """Test dialogue retrieval."""
        dialogue = pyhmong.basic_dialogue(1)
        self.assertIsInstance(dialogue, list)
        self.assertGreater(len(dialogue), 0)
        self.assertIsInstance(dialogue[0], tuple)


class TestNumbers(unittest.TestCase):
    """Test number and measure features."""
    
    def test_num_to_hmong(self):
        """Test number to Hmong conversion."""
        self.assertEqual(pyhmong.num_to_hmong(1), "ib")
        self.assertEqual(pyhmong.num_to_hmong(5), "tsib")
        self.assertEqual(pyhmong.num_to_hmong(10), "kaum")
    
    def test_hmong_to_num(self):
        """Test Hmong to number conversion."""
        self.assertEqual(pyhmong.hmong_to_num("ib"), 1)
        self.assertEqual(pyhmong.hmong_to_num("ob"), 2)
        self.assertEqual(pyhmong.hmong_to_num("kaum"), 10)
    
    def test_convert_measure(self):
        """Test measurement conversion."""
        result = pyhmong.convert_measure(10, "lbs", "kg")
        self.assertIn("4.54", result)


class TestProverbs(unittest.TestCase):
    """Test proverbs and idioms features."""
    
    def test_get_proverb(self):
        """Test proverb retrieval."""
        proverb = pyhmong.get_proverb("wisdom")
        self.assertIsInstance(proverb, str)
        self.assertGreater(len(proverb), 0)
    
    def test_explain_idiom(self):
        """Test idiom explanation."""
        explanation = pyhmong.explain_idiom("zoo siab")
        self.assertIn("happy", explanation.lower())


class TestEducation(unittest.TestCase):
    """Test education tools."""
    
    def test_generate_drill(self):
        """Test drill generation."""
        tone_drill = pyhmong.generate_drill("tone")
        self.assertIsInstance(tone_drill, list)
        self.assertGreater(len(tone_drill), 0)
        
        consonant_drill = pyhmong.generate_drill("consonant")
        self.assertIsInstance(consonant_drill, list)
    
    def test_quiz_flashcards(self):
        """Test flashcard quiz."""
        cards = pyhmong.quiz_flashcards("food")
        self.assertIsInstance(cards, dict)
        self.assertGreater(len(cards), 0)
    
    def test_check_pronunciation(self):
        """Test pronunciation checking."""
        analysis = pyhmong.check_pronunciation("kuv")
        self.assertIn("valid", analysis)
        self.assertIn("tone", analysis)
        self.assertTrue(analysis["valid"])


class TestIntegration(unittest.TestCase):
    """Integration tests combining multiple features."""
    
    def test_learning_workflow(self):
        """Test complete learning workflow."""
        # Get greeting
        greeting = pyhmong.get_greeting("general")
        self.assertIsInstance(greeting, str)
        
        # Translate words
        translation = pyhmong.translate_hm_to_en("kuv")
        self.assertIsInstance(translation, str)
        
        # Check grammar
        pos = pyhmong.detect_pos("kuv")
        self.assertEqual(pos, "pronoun")
        
        # Practice pronunciation
        drill = pyhmong.generate_drill("tone")
        self.assertIsInstance(drill, list)
    
    def test_sentence_processing(self):
        """Test processing a complete sentence."""
        sentence = "Kuv yog neeg Hmoob"
        
        # Tokenize
        tokens = pyhmong.tokenize(sentence)
        self.assertEqual(len(tokens), 4)
        
        # Check each word
        for token in tokens:
            is_valid = pyhmong.is_valid_syllable(token)
            self.assertTrue(is_valid)
        
        # Normalize
        normalized = pyhmong.normalize_text(sentence)
        self.assertIsInstance(normalized, str)
    
    def test_translation_roundtrip(self):
        """Test translation consistency."""
        # Translate Hmong to English
        hmong_word = "niam"
        english = pyhmong.translate_hm_to_en(hmong_word)
        self.assertIn("mother", english.lower())
        
        # Search should find it
        results = pyhmong.search_dictionary(hmong_word, "hm")
        self.assertGreater(len(results), 0)


class TestUtilities(unittest.TestCase):
    """Test utility functions."""
    
    def test_tokenize(self):
        """Test tokenization."""
        tokens = pyhmong.tokenize("Kuv yog neeg")
        self.assertEqual(tokens, ["Kuv", "yog", "neeg"])
    
    def test_is_valid_syllable(self):
        """Test syllable validation."""
        self.assertTrue(pyhmong.is_valid_syllable("kuv"))
        self.assertTrue(pyhmong.is_valid_syllable("ntxawg"))
        self.assertFalse(pyhmong.is_valid_syllable("xyz"))
    
    def test_decompose_syllable(self):
        """Test syllable decomposition."""
        parts = pyhmong.decompose_syllable("kuv")
        self.assertEqual(parts["onset"], "k")
        self.assertEqual(parts["nucleus"], "u")
        self.assertEqual(parts["coda"], "v")
    
    def test_count_syllables(self):
        """Test syllable counting."""
        count = pyhmong.count_syllables("Kuv yog neeg Hmoob")
        self.assertEqual(count, 4)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling."""
    
    def test_empty_input(self):
        """Test handling of empty input."""
        self.assertEqual(pyhmong.tokenize(""), [])
        self.assertEqual(pyhmong.normalize_text(""), "")
    
    def test_invalid_translation(self):
        """Test translation of unknown words."""
        result = pyhmong.translate_hm_to_en("xyzabc")
        self.assertIn("not found", result.lower())
    
    def test_invalid_tone_conversion(self):
        """Test tone conversion with invalid input."""
        # Should handle gracefully
        result = pyhmong.convert_tone("xyz", "b")
        self.assertIsInstance(result, str)
    
    def test_multiple_spaces(self):
        """Test normalization with multiple spaces."""
        result = pyhmong.normalize_text("kuv    yog     neeg")
        self.assertNotIn("  ", result)  # No double spaces
    
    def test_mixed_case(self):
        """Test normalization with mixed case."""
        result = pyhmong.normalize_text("KUV yOg NeEg")
        self.assertTrue(result[0].isupper())  # First letter capitalized
    
    def test_unknown_pos(self):
        """Test POS detection for unknown words."""
        pos = pyhmong.detect_pos("unknownword123")
        self.assertEqual(pos, "unknown")
    
    def test_large_numbers(self):
        """Test number conversion for larger values."""
        result = pyhmong.num_to_hmong(100)
        self.assertIn("pua", result)


class TestPerformance(unittest.TestCase):
    """Test performance with larger inputs."""
    
    def test_large_text_normalization(self):
        """Test normalization with large text."""
        large_text = "kuv yog neeg hmoob " * 100
        result = pyhmong.normalize_text(large_text)
        self.assertIsInstance(result, str)
    
    def test_multiple_translations(self):
        """Test multiple translations."""
        words = ["kuv", "koj", "nws", "peb", "nej"] * 20
        for word in words:
            result = pyhmong.translate_hm_to_en(word)
            self.assertIsInstance(result, str)
    
    def test_bulk_syllable_validation(self):
        """Test validating many syllables."""
        syllables = ["kuv", "koj", "nws"] * 50
        for syllable in syllables:
            result = pyhmong.is_valid_syllable(syllable)
            self.assertIsInstance(result, bool)


class TestDocumentation(unittest.TestCase):
    """Test that documentation examples work."""
    
    def test_readme_examples(self):
        """Test examples from README."""
        # From Quick Start
        clean = pyhmong.normalize_text("kuv  YOG  neeg")
        self.assertEqual(clean, "Kuv yog neeg")
        
        tone = pyhmong.get_tone("kuv")
        self.assertEqual(tone, "V")
        
        result = pyhmong.translate_hm_to_en("niam")
        self.assertIn("mother", result)
    
    def test_api_consistency(self):
        """Test that all API functions are accessible."""
        # Check all main functions exist
        functions = [
            'normalize_text',
            'syllable_split',
            'get_tone',
            'convert_tone',
            'translate_hm_to_en',
            'translate_en_to_hm',
            'search_dictionary',
            'detect_pos',
            'get_classifiers',
            'conjugate',
            'substitute',
            'get_greeting',
            'ask_question',
            'basic_dialogue',
            'num_to_hmong',
            'hmong_to_num',
            'convert_measure',
            'get_proverb',
            'explain_idiom',
            'generate_drill',
            'quiz_flashcards',
            'check_pronunciation',
        ]
        
        for func_name in functions:
            self.assertTrue(hasattr(pyhmong, func_name),
                          f"Function {func_name} not found in pyhmong")


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)