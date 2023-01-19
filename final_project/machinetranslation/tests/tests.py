import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_Hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_notTranslated(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")

    def test_Goodbye(self):
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

    def test_null_strings(self):
        self.assertEqual(english_to_french(), "The supplied string is empty")
        self.assertEqual(english_to_french(''), "The supplied string is empty")

class TestFrenchToEnglish(unittest.TestCase):
    def test_Hello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        
    def test_notTranslated(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        
    def test_Goodbye(self):
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        
    def test_null_strings(self):
        self.assertEqual(french_to_english(), "The supplied string is empty")
        self.assertEqual(french_to_english(''), "The supplied string is empty")

unittest.main()
