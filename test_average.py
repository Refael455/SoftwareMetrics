import unittest
from example_calculating_coverage import average, WD

class TestGrades(unittest.TestCase):

    def test_fail(self):
        self.assertEqual(average(10), 'Fail')
        
    def test_pass(self):
        self.assertEqual(average(60), "Pass")
        
    def test_passwithdistinction(self):
        self.assertEqual(average(90), WD)

    def test_isupper(self):
        with self.assertRaises(ValueError):
            average("gfhjdkl")
            
    def test_negative_number(self):
        #print(average(-1))
        with self.assertRaises(ValueError):
            average(-1)

if __name__ == '__main__':
    #print(average(-1))
    unittest.main(
        #defaultTest="TestGrades.test_negative_number"
        )
