import unittest
from translator import englishtofrench, frenchtoenglish

#unit test for English to  French Translation
class TestEnglishToFrench(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench("Hello"), "Bonjour")
        self.assertNotEqual(englishtofrench("Goodbye"), "Au Revoir")
        

#unit test for French to  English Translation
class TestFrenchToENglish(unittest.TestCase):
    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish("Bonjour"),"Hello")
        self.assertNotEqual(frenchtoenglish("Au Revoir"),"Goodbye")

 
if __name__ == '__main__':
    unittest.main()
    