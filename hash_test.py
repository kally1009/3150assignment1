import unittest
import hash
#from hash import Student
#from hash import Hash
#from hash import isPrime


class TestStudent(unittest.TestCase):
    def setUp(self):
        pass

    def test_getSSN(self):
        pass

    def test_getFirstname(self):
        pass

    def test_getLastname(self):
        pass

    def test_getEmail(self):
        pass

    def test_getAge(self):
        pass

    def test_eq(self):
        pass
        #How do I test these kinds of functions with overriding what == , >, <, and int?
    
    def test_isPrime_Prime(self): # not within a class...? 
        self.assertTrue(hash.isPrime(3),True) 
        self.assertTrue(hash.isPrime(1),True)
        self.assertTrue(hash.isPrime(2), True)
        self.assertTrue(hash.isPrime(5),True)
        self.assertTrue(hash.isPrime(7), True)
        self.assertTrue(hash.isPrime(19), True) 
        #test high numbers if prime or not
        #test negative numbers
    
    def test_isPrime_Prime_largeNumbers(self):
        self.assertTrue(hash.isPrime(487), True)
        self.assertTrue(hash.isPrime(499), True)
        self.assertTrue(hash.isPrime(6971), True)
        self.assertTrue(hash.isPrime(9679), True)
        self.assertTrue(hash.isPrime(11587), True)
        self.assertTrue(hash.isPrime(33469), True)


    def test_isPrime_notPrime(self):
        self.assertFalse(hash.isPrime(4),False)
        self.assertFalse(hash.isPrime(6),False)
        self.assertFalse(hash.isPrime(8),False)
        self.assertFalse(hash.isPrime(100), False)

    def test_isPrime_notPrime_LargeNumbers(self):
        self.assertFalse(hash.isPrime(100000), False)
        self.assertFalse(hash.isPrime(12000), False)
        self.assertFalse(hash.isPrime(2563), False)

    ##  self.assertFalse(hash.isPrime(-1),False) -> Raises an error, how to have it be expecting an error?
        #self.assertFalse(hash.isPrime(-7), False)
        #test if 4, 6, 8, 0? 
        #test high numbers
        #test negative numbers
        

   # def test_isPrime_notNone(self):
        #pass
        #self.assertIsNotNone 
        #test if x isn't or is none, and handled correctly (instead of crashing?)

    #def test_isPrime_None(self):
        #pass
        #test if it is none

    def test_hash_init_msize(self):
        newHash = hash.Hash(10)
        self.assertEqual(newHash.size(),0)
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
        
    def test_traverse(self):
        pass
    
    def test_delete(self):
        pass

if __name__ == '__main__':
    unittest.main()
