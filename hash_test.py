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

    def test_eq_with_differentStudent(self):
        # How do I test these kinds of functions with overriding what == , >, <, and int?
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__eq__(otherStudent))

    def test_eq_with_sameStudent(self):
        sameStudent = self.newStudent
        self.assertTrue(self.newStudent.__eq__(sameStudent))

    def test_gt_with_higherOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__gt__(otherStudent))

    def test_gt_with_lowerOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "100321", "anderson.com", 26)
        self.assertTrue(self.newStudent.__gt__(otherStudent))

    def test_lt_withHigherOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "654321", "anderson.com", 26)
        self.assertTrue(self.newStudent.__lt__(otherStudent))

    def test_lt_withLowerOther(self):
        otherStudent = hash.Student(
            "Anderson", "Porta", "100321", "anderson.com", 26)
        self.assertFalse(self.newStudent.__lt__(otherStudent))

    # TESTING INT METHOD WHERE ITS SUPPOSED TO CHANGE AN OBJECT TO AN INT BASED ON SSN

    def test_int_method(self):
        expectedSSN = 123456
        notExpectedSSN = 13456
        self.assertEqual(int(self.newStudent), expectedSSN)
        self.assertNotEqual(int(self.newStudent), notExpectedSSN)

    def test_isPrime_Prime(self):  # not within a class...?
        # Testing if 3 is prime? What do I do with self.something? Function not in a class.
        # self.assertTrue(hash.isPrime(3), True)
        # test if 1 and 2 and 5 and 7 and 9 is prime
        # test high numbers if prime or not
        # test negative numbers
        pass

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

    def test_Hash_Is_An_Instance_Of_Hash_With_Correct(self):
        self.assertIsInstance(self.newHash, hash.Hash)

    def test_Hash_Is_An_Instance_Of_Hash_With_Incorrect(self):
        self.assertNotIsInstance(self.newStudent, hash.Hash)

    def test_hash_init(self):
        pass
        # test the __init__ (figure out what exactly it is doing) Look at Bart's instructions on assignment?
        #

    def test_Insert(self):  # how to test this with files? Need to include files within test suite?
        pass

    def test_Retrieve_None(self):
        pass
        # does it return none when it doesn't exist?
        # return value... Look up what

    def test_Retrieve_value(self):
        pass

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
    # --------------TRAVERSE-------------------------

    def test_traverse(self):
        pass

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

    def test_Delete_With_Non_Student_Object(self):
        badStudent = hash.Hash(200)
        self.assertFalse(self.newHash.Delete(badStudent))


if __name__ == '__main__':
    unittest.main()
