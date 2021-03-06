import unittest
import hash
# from hash import Student
# from hash import Hash
# from hash import isPrime


class TestStudent(unittest.TestCase):

    # THIS RUNS EVERYTIME BEFORE ANY TEST.
    def setUp(self):
        self.newStudent = hash.Student("Jandir", "Porta", "123456", "jandir_porta@hotmail.com", 34)
        self.newHash = hash.Hash(30000)
        self.test_Student = self.newHash.Insert(self.newStudent)

    def test_newStudent_Object(self):
        newStudent1 = hash.Student("jfska","dkfas", "123789", "jan@gmail.com", 42)
        newStudent2 = hash.Student("jfska","dkfas", "123729", "jan@gmail.com", 46)
        newStudent3 = hash.Student("jfska","dkfas", "123789", "jan@gmail.com", 48)
        newStudent4 = hash.Student("jfska","dkfas", "123989", "jan@gmail.com", 53)
        self.assertTrue(newStudent1)
        self.assertTrue(newStudent2)
        self.assertTrue(newStudent3)
        self.assertTrue(newStudent4)

    def test_newStudent_Initialization_with_good_student_object(self):
        self.assertIsInstance(self.newStudent, hash.Student)

    def test_newStudent_Initialization_with_bad_student_object(self):
        testHash = hash.Hash(10)
        self.assertNotIsInstance(testHash, hash.Student)

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
        testStudentEmail = self.newStudent.getEmail()
        expectedEmail = "jandir_porta@hotmail.com"
        self.assertEqual(testStudentEmail, expectedEmail, "The emails dont match")

    def test_getAge(self):
        testStudentAge = self.newStudent.getAge()
        expectedAge = 34
        self.assertEqual(testStudentAge, expectedAge, "Both ages do not match")

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

    def test_hash_init_msize(self):
        newHash = hash.Hash(10)
        self.assertEqual(newHash.size(),0)

    def test_eq_with_differentStudent(self):
        # How do I test these kinds of functions with overriding what == , >, <, and int?
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__eq__(otherStudent))

    def test_eq_with_sameStudent(self):
        sameStudent = self.newStudent
        self.assertTrue(self.newStudent.__eq__(sameStudent))

    def test_eq_with_non_student_object(self):
        otherStudent = self.newHash
        self.assertFalse(self.newStudent.__eq__(otherStudent))

    def test_gt_with_higherOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__gt__(otherStudent))

    def test_gt_with_lowerOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "100321", "anderson.com", 26)
        self.assertTrue(self.newStudent.__gt__(otherStudent))

    def test_gt_with_non_student_object(self):
        otherStudent = self.newHash
        self.assertFalse(self.newStudent.__gt__(otherStudent))

    def test_lt_withHigherOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertTrue(self.newStudent.__lt__(otherStudent))

    def test_lt_withLowerOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "100321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__lt__(otherStudent))

    def test_lt_with_non_student_object(self):
        otherStudent = self.newHash
        self.assertFalse(self.newStudent.__lt__(otherStudent))

    # TESTING INT METHOD WHERE ITS SUPPOSED TO CHANGE AN OBJECT TO AN INT BASED ON SSN

    def test_int_method(self):
        expectedSSN = 123456
        notExpectedSSN = 13456
        self.assertEqual(int(self.newStudent), expectedSSN)
        self.assertNotEqual(int(self.newStudent), notExpectedSSN)


    def test_isPrime_notPrime_specialCase_1_and_0(self):
        self.assertFalse(hash.isPrime(0), False)
        self.assertFalse(hash.isPrime(1), False)

    def test_Hash_Initialization(self):
        testHash1 = hash.Hash(30)
        testHash2= hash.Hash(60)
        testHash3 = hash.Hash(50)
        testHash4 = hash.Hash(30)
        self.assertTrue(testHash1)
        self.assertTrue(testHash2)
        self.assertTrue(testHash3)
        self.assertTrue(testHash4)
    def test_isPrime_notPrime_specialCase_String(self):
        self.assertFalse(hash.isPrime('7'), False)
        self.assertFalse(hash.isPrime('11'), False)

    

    def test_hash_init_msize(self):
        self.assertEqual(self.newHash.size(),1) #It's one because in the setUp we insert a student right away.

    def test_Insert_True(self):
        self.assertTrue(self.newHash.Insert(213-45-6789), True)
        self.assertTrue(self.newHash.Insert(313-45-6789), True)
        self.assertTrue(self.newHash.Insert(413-45-6789), True)
        
    def test_Hash_Is_An_Instance_Of_Hash_With_Correct(self):
        self.assertIsInstance(self.newHash, hash.Hash)

    def test_Hash_Is_An_Instance_Of_Hash_With_Incorrect(self):
        self.assertNotIsInstance(self.newStudent, hash.Hash)

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
        self.assertTrue(self.newHash.Exists(self.newStudent))

    # testing with something that doesnt exist
    def test_Exists_With_N0_EXIST(self):
        newStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newHash.Exists(newStudent))

    def test_Exists_With_None_Item(self):
        self.assertIsNone(self.newHash.Exists(None))


    # -----------------DELETE------------------------------
    def test_delete_with_existing_item(self):
        # self.newHash.Insert(self.newStudent)
        self.assertTrue(self.newHash.Delete(self.newStudent))
        # CHECKING IF IT ACTUALLY DELETED THE STUDENT
        self.assertFalse(self.newHash.Exists(self.newStudent))

    def test_Delete_With_Non_Existing_Item(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newHash.Delete(otherStudent))
        self.assertFalse(self.newHash.Delete("otherStudent"))
        self.assertFalse(self.newHash.Delete(1234))

    def test_Delete_With_Non_Student_Object(self):
        badStudent = hash.Hash(200)
        self.assertFalse(self.newHash.Delete(badStudent))

    def test_addAges_regular(self):
        student1 = hash.Student('Kally', 'Adams', '098-76-5432', 'kallyadams@email.com', '22')
        student2 = hash.Student('Rob', 'Albert', '123-45-6789', 'robalbert@dixie.edu', '49')
        self.assertEqual(hash.addAges(student1), 44)
        self.assertEqual(hash.addAges(student2), 93)
        self.assertEqual(hash.addAges(self.newStudent), 127)

    def test_addAges_and_init_not_int(self):
        student3 = hash.Student('Kally', 'Adams', '198-76-5432', 'kallyadams@email.com', 22.5)
        self.assertEqual(hash.addAges(student3), 22)

    def test_addAges_None_Item(self):
        with self.assertRaises(Exception):
            student0 = hash.Student(None,None,None,None)
    def test_addAges_age_None(self):
        with self.assertRaises(Exception):
            student0 = hash.Student('Kal','Adam', '901-76-7890', 'kaladam@email.com', None)
    
    def test_addAges_notAnObject_but_int(self):
        self.assertFalse(hash.addAges(0), False)

    def test_addAges_notAnObject_but_string(self):
        self.assertFalse(hash.addAges('hi'), False)

    def test_Delete_With_None_Item(self):
        self.assertIsNone(self.newHash.Delete(None))

    
if __name__ == '__main__':
    unittest.main()
