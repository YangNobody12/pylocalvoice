"""
Examples of using the pyhmong library
======================================

This file contains various examples demonstrating the features of pyhmong.
"""

from pyhmong import (
    HmongProcessor,
    HmongDictionary,
    RomanizationSystem,
    ToneMarker,
    tokenize,
    is_valid_syllable,
    normalize
)


def example_basic_usage():
    """Basic usage examples."""
    print("=" * 60)
    print("BASIC USAGE EXAMPLES")
    print("=" * 60)
    
    # Simple tokenization
    text = "Kuv yog neeg Hmoob"
    tokens = tokenize(text)
    print(f"\nText: {text}")
    print(f"Tokens: {tokens}")
    
    # Syllable validation
    print("\nSyllable Validation:")
    syllables = ["kuv", "koj", "xyz", "ntxawg"]
    for syllable in syllables:
        valid = is_valid_syllable(syllable)
        print(f"  {syllable}: {'✓ Valid' if valid else '✗ Invalid'}")
    
    # Text normalization
    messy_text = "kuv   yog  NEEG    hmoob"
    normalized = normalize(messy_text)
    print(f"\nOriginal:   '{messy_text}'")
    print(f"Normalized: '{normalized}'")


def example_processor():
    """Examples using HmongProcessor class."""
    print("\n" + "=" * 60)
    print("HMONG PROCESSOR EXAMPLES")
    print("=" * 60)
    
    processor = HmongProcessor()
    
    # Tokenization
    text = "Nyob zoo, koj nyob li cas?"
    print(f"\nText: {text}")
    print(f"Tokens: {processor.tokenize(text)}")
    print(f"Syllable count: {processor.count_syllables(text)}")
    
    # Tone analysis
    print("\nTone Analysis:")
    words = ["kuv", "koj", "nws", "peb", "zoo"]
    for word in words:
        tone = processor.get_tone(word)
        print(f"  {word} → {tone.name}: {tone.value}")
    
    # Syllable decomposition
    print("\nSyllable Decomposition:")
    syllables = ["kuv", "ntxawg", "zoo", "hmoob"]
    for syllable in syllables:
        parts = processor.decompose_syllable(syllable)
        print(f"  {syllable}:")
        print(f"    Onset:   {parts['onset']}")
        print(f"    Nucleus: {parts['nucleus']}")
        print(f"    Coda:    {parts['coda']}")


def example_dictionary():
    """Examples using HmongDictionary class."""
    print("\n" + "=" * 60)
    print("DICTIONARY EXAMPLES")
    print("=" * 60)
    
    dictionary = HmongDictionary()
    
    # Look up words
    print("\nDictionary Lookups:")
    words = ["kuv", "koj", "nws", "peb", "yog", "zoo"]
    for word in words:
        definition = dictionary.lookup(word)
        print(f"  {word}: {definition}")
    
    # Add custom words
    print("\nAdding Custom Words:")
    custom_words = {
        "tsev": "house",
        "txiv": "father",
        "niam": "mother",
        "tub": "son"
    }
    
    for word, definition in custom_words.items():
        dictionary.add_word(word, definition)
        print(f"  Added: {word} = {definition}")
    
    # Show all words
    all_words = dictionary.get_all_words()
    print(f"\nTotal words in dictionary: {len(all_words)}")
    print(f"First 10 words: {', '.join(all_words[:10])}")


def example_linguistic_analysis():
    """Examples of linguistic analysis."""
    print("\n" + "=" * 60)
    print("LINGUISTIC ANALYSIS EXAMPLES")
    print("=" * 60)
    
    processor = HmongProcessor()
    
    # Get phonological components
    consonants = processor.get_initial_consonants()
    vowels = processor.get_vowels()
    
    print(f"\nHmong Phonology (RPA System):")
    print(f"  Total consonants: {len(consonants)}")
    print(f"  Total vowels: {len(vowels)}")
    print(f"  Total tones: {len(processor.TONES)}")
    
    # Sample consonants
    print(f"\n  Sample consonants:")
    print(f"    Single: {', '.join(processor.CONSONANTS['single'][:10])}")
    print(f"    Digraphs: {', '.join(processor.CONSONANTS['digraphs'][:5])}")
    print(f"    Trigraphs: {', '.join(processor.CONSONANTS['trigraphs'][:3])}")
    
    # Sample vowels
    print(f"\n  Sample vowels:")
    print(f"    Simple: {', '.join([v for v in processor.VOWELS if len(v) == 1])}")
    print(f"    Complex: {', '.join([v for v in processor.VOWELS if len(v) > 1][:5])}")


def example_text_processing_pipeline():
    """Example of a complete text processing pipeline."""
    print("\n" + "=" * 60)
    print("TEXT PROCESSING PIPELINE")
    print("=" * 60)
    
    processor = HmongProcessor()
    dictionary = HmongDictionary()
    
    # Sample Hmong text
    texts = [
        "Kuv yog neeg Hmoob",
        "Koj nyob qhov twg?",
        "Peb mus tsev",
        "Nyob zoo koj nyob li cas"
    ]
    
    for i, text in enumerate(texts, 1):
        print(f"\n--- Text {i} ---")
        print(f"Original: {text}")
        
        # Normalize
        normalized = processor.normalize(text)
        print(f"Normalized: {normalized}")
        
        # Tokenize
        tokens = processor.tokenize(text)
        print(f"Tokens: {tokens}")
        
        # Analyze each token
        print("Analysis:")
        for token in tokens:
            valid = processor.is_valid_syllable(token)
            tone = processor.get_tone(token)
            definition = dictionary.lookup(token)
            
            status = "✓" if valid else "✗"
            def_str = f" → {definition}" if definition else ""
            print(f"  {status} {token} [{tone.name}]{def_str}")


def example_validation():
    """Examples of input validation."""
    print("\n" + "=" * 60)
    print("VALIDATION EXAMPLES")
    print("=" * 60)
    
    processor = HmongProcessor()
    
    # Test various inputs
    test_cases = [
        ("kuv", "Valid Hmong word"),
        ("ntxawg", "Valid with trigraph onset"),
        ("xyz", "Invalid combination"),
        ("Hmoob", "Valid with capitalization"),
        ("hello", "English word"),
        ("123", "Numbers only"),
        ("", "Empty string"),
    ]
    
    print("\nValidation Tests:")
    for syllable, description in test_cases:
        valid = processor.is_valid_syllable(syllable)
        result = "✓ VALID" if valid else "✗ INVALID"
        print(f"  {result} | '{syllable}' - {description}")


def example_advanced_features():
    """Examples of advanced features."""
    print("\n" + "=" * 60)
    print("ADVANCED FEATURES")
    print("=" * 60)
    
    # Create processor with specific romanization system
    processor = HmongProcessor(system=RomanizationSystem.RPA)
    
    print(f"\nRomanization System: {processor.system.value}")
    
    # Batch processing
    print("\nBatch Processing:")
    sentences = [
        "Kuv yog neeg Hmoob",
        "Koj puas tau mus tsev?",
        "Peb nyob hauv lub nroog"
    ]
    
    for sentence in sentences:
        tokens = processor.tokenize(sentence)
        count = processor.count_syllables(sentence)
        print(f"  '{sentence}'")
        print(f"    Tokens: {count} syllables")
        
        # Count tones
        tone_counts = {}
        for token in tokens:
            tone = processor.get_tone(token)
            tone_counts[tone.name] = tone_counts.get(tone.name, 0) + 1
        
        print(f"    Tones: {dict(tone_counts)}")


def main():
    """Run all examples."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 15 + "PYHMONG LIBRARY EXAMPLES" + " " * 19 + "║")
    print("╚" + "=" * 58 + "╝")
    
    example_basic_usage()
    example_processor()
    example_dictionary()
    example_linguistic_analysis()
    example_text_processing_pipeline()
    example_validation()
    example_advanced_features()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()