'''
Created on Jan 23, 2014

@author: mokter
'''
import unittest


class Test(unittest.TestCase):

    def testAddition(self):
        
        self.assertEqual(1+1,2)
        self.failUnlessEqual(1+1,2)
        
        self.failIfEqual(1+1,1)
                
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAddition']
    unittest.main()