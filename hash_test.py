import unittest
import hash
#from hash import Student
#from hash import Hash
#from hash import isPrime


class TestStudent(unittest.TestCase):

    # THIS RUNS EVERYTIME BEFORE ANY TEST.
    def setUp(self):
        self.newStudent = hash.Student("Jandir", "Porta", "123456", "jandir_porta@hotmail.com", 34)

        self.newHash = hash.Hash(10)

    def test_getSSN(self):
        testStudentSSN = self.newStudent.getSSN()
        expectedSSN = "123456"
        self.assertEqual(testStudentSSN, expectedSSN, "The SSN do not match")

    def test_getFirstname(self):
        testStudentFirstName = self.newStudent.getFirstName()
        expectedFirstName = "Jandir"
        self.assertIs(testStudentFirstName, expectedFirstName,
                      "The first names dont match")

    def test_getLastname(self):
        testStudentLastName = self.newStudent.getLastName()
        expectedLastName = "Porta"
        self.assertEqual(testStudentLastName, expectedLastName,
                         "The Last names dont match")

    # def test_getEmail(self):
    #     testStudentEmail = self.newStudent.getEmail()
    #     expectedEmail = "jandir_porta@hotmail.com"
    #     self.assertIs(testStudentEmail, expectedEmail, "The email do not match")

    def test_getAge(self):
        testStudentAge = self.newStudent.getAge()
        expectedAge = 34
        self.assertEqual(testStudentAge, expectedAge, "Both ages do not match")

    def test_eq(self):
        #How do I test these kinds of functions with overriding what == , >, <, and int?
        pass

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
    def test_isPrime_Prime(self):  # not within a class...?
        # Testing if 3 is prime? What do I do with self.something? Function not in a class.
        self.assertTrue(hash.isPrime(3), True)
        # test if 1 and 2 and 5 and 7 and 9 is prime
        # test high numbers if prime or not
        # test negative numbers

    def test_isPrime_notPrime(self):
        # self.assertFalse(self(4),False)
        # test if 4, 6, 8, 0?
        # test high numbers
        # test negative numbers
        pass

    def test_isPrime_notNone(self):
        pass
        # self.assertIsNotNone
        # test if x isn't or is none, and handled correctly (instead of crashing?)

    def test_isPrime_None(self):
        pass
        # test if it is none

    def test_hash_init(self):
        pass
        # test the __init__ (figure out what exactly it is doing) Look at Bart's instructions on assignment?
        #

    def test_Insert(self):  # how to test this with files? Need to include files within test suite?

        pass

    def test_Retrieve_None(self):
        pass

        #does it return none when it doesn't exist?
        #return value... Look up what (a count?) returns anything but none...
        # does it return none when it doesn't exist?
        # return value... Look up what

    def test_Retrieve_value(self):
        pass

    # ---------------------------EXISTS----------------------------
    # test with something that exists
    def test_Exists_With_EXISTS(self):
        self.newHash.Insert(self.newStudent)
        self.assertTrue(self.newHash.Exists(self.newStudent))

    # testing with something that doesnt exist
    def test_Exists_With_N0_EXIST(self):
        # existingStudent = hash.Student("FRANK","ELLIS","497-45-2922","ELLIS.FRANK@Dixie.edu", 47)
        # self.assertTrue(hash.Hash.Exists(existingStudent))
        pass

    # --------------TRAVERSE-------------------------
    def test_traverse(self):
        pass
    
    # -----------------DELETE------------------------------
    def test_delete(self):
        pass


if __name__ == '__main__':
    unittest.main()
