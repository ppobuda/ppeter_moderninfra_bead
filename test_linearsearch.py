import linearsearch
import unittest

class testCases(unittest.TestCase):

    

    def test_Match(self):
        array = [1,2,3,4,5]
        self.assertEqual(linearsearch.linearSearch(array,5),4)

    def test_multipleOccurence(self):
        array = [1,2,3,3,5]
        self.assertEqual(linearsearch.linearSearch(array,3),2)

    def test_misMatch(self):
        array = [1,2,3,4,5]
        self.assertEqual(linearsearch.linearSearch(array,99),-1)


if __name__ == '__main__':
    unittest.main()