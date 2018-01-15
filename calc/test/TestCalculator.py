'''
Created on Jan 23, 2014

@author: mokter
'''
import unittest

#from calc.test.Calculator import Calculator
from calc.test.Calculator import *


class TestCalculator(unittest.TestCase):
    
    def testAdd(self):
        calc = Calculator()
        result = calc.add(op1=5, op2=5)
        self.assertEqual(result, 10, "Oops!! Addition failed")
        
        
if __name__ == "__main__":
    
    #import sys;sys.argv = ['', 'Test.testAdd']
    unittest.main()