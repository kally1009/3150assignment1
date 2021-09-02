import unittest
from hash import Student
from hash import Hash


class TestStudent(unittest.TestCase):
    def setup(self):
        pass
    
    def test_isPrime_Prime(self): # not within a class...? 
        self.assertTrue(self(3),True) #Testing if 3 is prime
        #test if 1 and 2 and 5 and 7 and 9 is prime 
        #test high numbers if prime or not
        #test negative numbers
        
    def test_isPrime_notPrime(self):
        self.assertFalse(self(4),False)
        #test if 4, 6, 8, 0? 
        #test high numbers
        #test negative numbers

    def test_isPrime_notNone(self):
        pass
        #self.assertIsNotNone 
        #test if x isn't or is none, and handled correctly (instead of crashing?)

    def test_isPrime_None(self):
        pass
        #test if it is none

    def test_hash_init(self):
        pass
        #test the __init__ (figure out what exactly it is doing) Look at Bart's instructions on assignment?
        #
    def test_Insert(self):  #how to test this with files? Need to include files within test suite?
        pass
    
    def test_Retrieve_None(self):
        pass
        #does it return none when it doesn't exist?
        #return value... Look up what 
    def test_Retrieve_value(self):
        pass


    def test_Exists(self):
        pass
        
    
