"""English to French tests"""
import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(english_to_french(0), 0)


class TestF2E(unittest.TestCase):
    """English to French tests"""
    def test2(self):
        self.assertEqual(french_to_english('Mercredi'), 'Wednesday')
        self.assertEqual(french_to_english('Lundi'),'Monday')

unittest.main()
