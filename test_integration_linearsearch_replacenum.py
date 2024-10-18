import linearsearch
import replacenum
import unittest

class integrationTests(unittest.TestCase):

    #first replace a num, then search if it is found at the given idx
    def test_integration(self):
        array = [1,2,3,4,5]
        replacenum.replaceNum(array,2,99)
        print(array)
        self.assertEqual(linearsearch.linearSearch(array,99),2)

if __name__ == '__main__':
    unittest.main()