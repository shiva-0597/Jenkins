import unittest
import calc

class Test_Calc(unittest.TestCase):

    def test_add(self):
        result=calc.add(10,15)
        self.assertEqual(result,25)

    def test_subtract(self):
        result=calc.subtract(10,5)
        self.assertEqual(result,5)

    def test_multiply(self):
        result=calc.multiply(10,2)
        self.assertEqual(result,20)
    
    def test_divide(self):
        result=calc.divide(10,2)
        self.assertEqual(result,5)