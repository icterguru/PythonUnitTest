'''
Created on Jan 23, 2014

@author: mokter
'''

class Student(object):
    '''
    classdocs
    '''
    
    def __init__(self, fname = "", lname = ""):
        
        '''  
        Constructor
        
        '''
        
        self.fname = fname
        self.lname = lname

    
    def __str__(self):
        return self.fname + " " + self.lname
        
s1 = Student("Mokter", "Hossain")
s2 = Student("Mahdi", "Munim")

print "\n"
print s1
print s2

