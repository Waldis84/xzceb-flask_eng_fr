import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        text1 = "Hello"
        translation1 = english_to_french(text1)
        self.assertEqual(translation1, "Bonjour")
        
        text2 = "Goodbye"
        translation2 = english_to_french(text2)
        self.assertEqual(translation2, "Au revoir")

        null_text = None
        with self.assertRaises(ValueError):
            english_to_french(null_text)
        
    def test_french_to_english(self):
        text1 = "Bonjour"
        translation1 = french_to_english(text1)
        self.assertEqual(translation1, "Hello")
        
        text2 = "Au revoir"
        translation2 = french_to_english(text2)
        self.assertEqual(translation2, "Goodbye")

        null_text = None
        with self.assertRaises(ValueError):
            french_to_english(null_text)
        
if __name__ == '__main__':
    unittest.main()