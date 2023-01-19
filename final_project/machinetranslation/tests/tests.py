import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
        self.assertEqual(english_to_french(), "The supplied string is empty")
        self.assertEqual(english_to_french(''), "The supplied string is empty")

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
        self.assertEqual(french_to_english(), "The supplied string is empty")
        self.assertEqual(french_to_english(''), "The supplied string is empty")

unittest.main()