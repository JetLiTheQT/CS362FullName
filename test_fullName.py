import unittest
import fullName

class testFullName(unittest.TestCase):
    def test_apostropheNames(self):
        #Passing Test
        self.assertEqual(fullName.fullName("D'Amato", "Lexington"), "D'Amato Lexington")
        #Failing Test
        #self.assertEqual(fullName.fullName("D'Amato", "Lexington"), "D'AmatoLexington")
    def test_randomStrings(self):
        #Passing Test
        self.assertEqual(fullName.fullName("123,&Hane", "Po'9zna\]"), "123,&Hane Po'9zna\]" )
        #Failing Test
        #self.assertEqual(fullName.fullName("123,&Hane", "Po'9zna\]"), "123,&Hane Po'9zna\" )
    def test_noInput(self):
        #Passing Test
        self.assertEqual(fullName.fullName("", ""), " ")
        #Failing Test
        #self.assertEqual(fullName.fullName("", ""), "")
if __name__ == '__main__':
    unittest.main()