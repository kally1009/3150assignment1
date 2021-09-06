import unittest
import hash
#from hash import Student
#from hash import Hash
#from hash import isPrime


class TestStudent(unittest.TestCase):

    # THIS RUNS EVERYTIME BEFORE ANY TEST.
    def setUp(self):
        self.newStudent = hash.Student("Jandir", "Porta", "123456", "jandir_porta@hotmail.com", 34)
        self.newHash = hash.Hash(30000)
        self.test_Student = self.newHash.Insert(self.newStudent)
        

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

    def test_getEmail(self):
        pass
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
        self.assertTrue(hash.isPrime(23),True)
        self.assertTrue(hash.isPrime(2), True)
        self.assertTrue(hash.isPrime(5),True)
        self.assertTrue(hash.isPrime(7), True)
        self.assertTrue(hash.isPrime(19), True) 
    
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

    def test_istPrime_Negative_Numbers(self):
        self.assertFalse(hash.isPrime(-1),False) 
        self.assertFalse(hash.isPrime(-7), False)
        
    def test_isPrime_positive_float_Numbers(self):
        self.assertFalse(hash.isPrime(1.5), False)
        self.assertFalse(hash.isPrime(98473721.1), False)
        self.assertFalse(hash.isPrime(91.1), False)
        self.assertFalse(hash.isPrime(1.0), False)
    
    def test_isPrime_negative_float_Numbers(self):
        self.assertFalse(hash.isPrime(-3.6),False)
        self.assertFalse(hash.isPrime(-99.1), False)
        self.assertFalse(hash.isPrime(-1.0), False)

    def test_isPrime_notNone(self):
        self.assertIsNotNone(hash.isPrime(2), not None)
        self.assertIsNotNone(hash.isPrime(3), not None) 
        #test if x isn't or is none, and handled correctly (instead of crashing?)

    def test_isPrime_None(self):
        self.assertIsNone(hash.isPrime(None), None)

    def test_isPrime_notPrime_specialCase_1_and_0(self):
        self.assertFalse(hash.isPrime(0), False)
        self.assertFalse(hash.isPrime(1), False)


    def test_hash_init_msize(self):
        self.assertEqual(self.newHash.size(),1) #It's one because in the setUp we insert a student right away.

    def test_Insert_True(self):
        self.assertTrue(self.newHash.Insert(213-45-6789), True)
        self.assertTrue(self.newHash.Insert(313-45-6789), True)
        self.assertTrue(self.newHash.Insert(413-45-6789), True)
        

    def test_insert_True_then_False(self):
        self.assertTrue(self.newHash.Insert(987-65-4321), True)
        self.assertFalse(self.newHash.Insert(987-65-4321), False)
        self.assertTrue(self.newHash.Insert(543-21-6789), True)
        self.assertFalse(self.newHash.Insert(543-21-6789), False)

    def test_Insert_False(self):
        self.assertFalse(self.newHash.Insert(self.newStudent), False)

    def test_Retrieve_None(self):
        self.assertIsNone(self.newHash.Retrieve(987-65-4321), None)
        self.assertIsNone(self.newHash.Retrieve(543-21-6789), None)

    def test_Retrieve_not_none(self):
        self.assertIsNotNone(self.newHash.Retrieve(self.newStudent), not None)
        

    # ---------------------------EXISTS----------------------------
    # test with something that exists
    def test_Exists_With_EXISTS(self):
       # self.newHash.Insert(self.newStudent)
       # self.assertTrue(self.newHash.Exists(self.newStudent), True)
        pass
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
