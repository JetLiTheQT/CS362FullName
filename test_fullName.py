import unittest
import fullName

class testFullName(unittest.TestCase):
    def test_apostropheNames(self):
        self.assertEqual(fullName.fullName("D'Amato", "Lexington"), "D'Amato Lexington")
    def test_randomStrings(self):
        self.assertEqual(fullName.fullName("123,&Hane", "Po'9zna\]"), "123,&Hane Po'9zna\]" )
    def test_noInput(self):
        self.assertEqual(fullName.fullName("", ""), " ")
if __name__ == '__main__':
    unittest.main()