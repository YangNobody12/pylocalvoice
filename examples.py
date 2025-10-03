"""
PyHmong Extended Examples
=========================

Demonstrates all 7 feature categories
"""

import pyhmong


def demo_phonology():
    """Demo 1: Phonology & Orthography"""
    print("=" * 70)
    print("1. PHONOLOGY & ORTHOGRAPHY")
    print("=" * 70)
    
    # Text normalization
    messy = "kuv   YOG  neeg   HMOOB"
    clean = pyhmong.normalize_text(messy)
    print(f"\n📝 Text Normalization:")
    print(f"  Before: '{messy}'")
    print(f"  After:  '{clean}'")
    
    # Syllable splitting
    text = "Nyob zoo"
    syllables = pyhmong.syllable_split(text)
    print(f"\n✂️  Syllable Split:")
    print(f"  Text: '{text}' → {syllables}")
    
    # Tone detection
    words = ["kuv", "koj", "zoo", "peb"]
    print(f"\n🎵 Tone Detection:")
    for word in words:
        tone = pyhmong.get_tone(word)
        print(f"  {word} → tone: {tone}")
    
    # Tone conversion
    print(f"\n🔄 Tone Conversion:")
    original = "kuv"
    for tone in ['b', 'j', 's', 'g']:
        converted = pyhmong.convert_tone(original, tone)
        print(f"  {original} → {converted} (tone {tone})")
    print()


def demo_translation():
    """Demo 2: Dictionary & Translation"""
    print("=" * 70)
    print("2. DICTIONARY & TRANSLATION")
    print("=" * 70)
    
    # Hmong to English
    print(f"\n📖 Hmong → English:")
    hmong_words = ["kuv", "koj", "nyob", "zoo", "tsev"]
    for word in hmong_words:
        translation = pyhmong.translate_hm_to_en(word)
        print(f"  {word} → {translation}")
    
    # English to Hmong
    print(f"\n📖 English → Hmong:")
    english_words = ["mother", "father", "house", "good"]
    for word in english_words:
        translation = pyhmong.translate_en_to_hm(word)
        print(f"  {word} → {translation}")
    
    # Dictionary search
    print(f"\n🔍 Dictionary Search:")
    results = pyhmong.search_dictionary("niam", lang="hm")
    for result in results[:3]:
        print(f"  {result}")
    print()


def demo_grammar():
    """Demo 3: Grammar"""
    print("=" * 70)
    print("3. GRAMMAR")
    print("=" * 70)
    
    # Part of speech detection
    print(f"\n🏷️  Part of Speech:")
    words = ["kuv", "yog", "tus", "neeg"]
    for word in words:
        pos = pyhmong.detect_pos(word)
        print(f"  {word} → {pos}")
    
    # Classifiers
    print(f"\n📊 Classifiers:")
    nouns = ["neeg", "tsev", "dev"]
    for noun in nouns:
        classifiers = pyhmong.get_classifiers(noun)
        print(f"  {noun} → {', '.join(classifiers)}")
    
    # Conjugation
    print(f"\n⏰ Conjugation:")
    sentence = "Kuv mus tsev"
    for tense in ["present", "past", "future"]:
        conjugated = pyhmong.conjugate(sentence, tense)
        print(f"  {tense}: {conjugated}")
    
    # Substitution drill
    print(f"\n🔄 Substitution:")
    original = "Kuv yog neeg Hmoob"
    replaced = pyhmong.substitute(original, "Kuv", "Koj")
    print(f"  Original: {original}")
    print(f"  Replaced: {replaced}")
    print()


def demo_phrasebook():
    """Demo 4: Phrasebook"""
    print("=" * 70)
    print("4. PHRASEBOOK UTILITIES")
    print("=" * 70)
    
    # Greetings
    print(f"\n👋 Greetings:")
    times = ["morning", "afternoon", "evening", "general"]
    for time in times:
        greeting = pyhmong.get_greeting(time)
        print(f"  {time}: {greeting}")
    
    # Questions
    print(f"\n❓ Common Questions:")
    topics = ["name", "age", "from", "doing"]
    for topic in topics:
        question = pyhmong.ask_question(topic)
        print(f"  {topic}: {question}")
    
    # Dialogues
    print(f"\n💬 Basic Dialogue (Unit 1):")
    dialogue = pyhmong.basic_dialogue(1)
    for hmong, english in dialogue:
        print(f"  {hmong}")
        print(f"  → {english}")
        print()


def demo_numbers():
    """Demo 5: Numbers & Measures"""
    print("=" * 70)
    print("5. NUMBERS & MEASURES")
    print("=" * 70)
    
    # Number to Hmong
    print(f"\n🔢 Numbers → Hmong:")
    numbers = [1, 5, 10, 15, 20, 100]
    for num in numbers:
        hmong = pyhmong.num_to_hmong(num)
        print(f"  {num} → {hmong}")
    
    # Hmong to Number
    print(f"\n🔢 Hmong → Numbers:")
    hmong_nums = ["ib", "ob", "kaum", "kaum tsib"]
    for word in hmong_nums:
        num = pyhmong.hmong_to_num(word)
        print(f"  {word} → {num}")
    
    # Measure conversions
    print(f"\n📏 Measure Conversions:")
    conversions = [
        (10, "lbs", "kg"),
        (5, "miles", "km"),
        (100, "feet", "meters"),
    ]
    for value, from_unit, to_unit in conversions:
        result = pyhmong.convert_measure(value, from_unit, to_unit)
        print(f"  {result}")
    print()


def demo_proverbs():
    """Demo 6: Proverbs & Idioms"""
    print("=" * 70)
    print("6. PROVERBS & IDIOMS")
    print("=" * 70)
    
    # Proverbs
    print(f"\n💭 Hmong Proverbs:")
    topics = ["wisdom", "family", "work"]
    for topic in topics:
        proverb = pyhmong.get_proverb(topic)
        print(f"  {topic}: {proverb}")
    
    # Idioms
    print(f"\n🗣️  Idiom Explanations:")
    idioms = ["zoo siab", "siab phem", "siab ntev"]
    for idiom in idioms:
        explanation = pyhmong.explain_idiom(idiom)
        print(f"  {idiom} → {explanation}")
    print()


def demo_education():
    """Demo 7: Education Tools"""
    print("=" * 70)
    print("7. EDUCATION TOOLS")
    print("=" * 70)
    
    # Pronunciation drills
    print(f"\n🗣️  Pronunciation Drills:")
    for drill_type in ["tone", "consonant", "vowel"]:
        drill = pyhmong.generate_drill(drill_type)
        print(f"  {drill_type}: {', '.join(drill)}")
    
    # Flashcards
    print(f"\n🃏 Flashcard Quiz:")
    categories = ["food", "family", "colors"]
    for category in categories:
        cards = pyhmong.quiz_flashcards(category)
        print(f"  {category.upper()}:")
        for hmong, english in list(cards.items())[:3]:
            print(f"    {hmong} = {english}")
    
    # Pronunciation check
    print(f"\n✅ Pronunciation Check:")
    words = ["kuv", "ntxawg", "zoo"]
    for word in words:
        analysis = pyhmong.check_pronunciation(word)
        print(f"  {word}:")
        print(f"    Valid: {analysis['valid']}")
        print(f"    Onset: {analysis['onset']}")
        print(f"    Nucleus: {analysis['nucleus']}")
        print(f"    Tone: {analysis['tone']}")
    print()


def demo_complete_workflow():
    """Demo: Complete workflow example"""
    print("=" * 70)
    print("COMPLETE WORKFLOW EXAMPLE")
    print("=" * 70)
    
    print(f"\n🎓 Learning Scenario: Introducing Yourself")
    print("-" * 70)
    
    # Step 1: Learn greeting
    greeting = pyhmong.get_greeting("general")
    print(f"\n1️⃣  Greeting: {greeting}")
    
    # Step 2: Learn to ask name
    question = pyhmong.ask_question("name")
    print(f"2️⃣  Ask name: {question}")
    
    # Step 3: Build response
    print(f"\n3️⃣  Build response:")
    words = ["kuv", "lub", "npe", "hu", "ua"]
    for word in words:
        translation = pyhmong.translate_hm_to_en(word)
        print(f"   {word} = {translation}")
    
    # Step 4: Practice pronunciation
    print(f"\n4️⃣  Practice pronunciation:")
    practice_word = "kuv"
    tones = ['b', 'j', 'v']
    print(f"   Base: {practice_word}")
    for tone in tones:
        variant = pyhmong.convert_tone(practice_word, tone)
        print(f"   → {variant} (tone {tone})")
    
    # Step 5: Complete dialogue
    print(f"\n5️⃣  Complete dialogue:")
    dialogue = pyhmong.basic_dialogue(1)
    for i, (hmong, english) in enumerate(dialogue[:2], 1):
        print(f"   {i}. {hmong}")
        print(f"      ({english})")
    
    print(f"\n✨ You're ready to introduce yourself in Hmong!")
    print()


def main():
    """Run all demonstrations"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "PYHMONG - ALL FEATURES DEMO" + " " * 25 + "║")
    print("╚" + "=" * 68 + "╝")
    print()
    
    demos = [
        demo_phonology,
        demo_translation,
        demo_grammar,
        demo_phrasebook,
        demo_numbers,
        demo_proverbs,
        demo_education,
        demo_complete_workflow,
    ]
    
    for demo in demos:
        demo()
        input("Press Enter to continue...")
        print("\n")
    
    print("=" * 70)
    print("🎉 All demos completed!")
    print("=" * 70)
    print()


if __name__ == "__main__":
    main()