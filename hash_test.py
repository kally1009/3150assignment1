import unittest
import hash
# from hash import Student
# from hash import Hash
# from hash import isPrime


class TestStudent(unittest.TestCase):
    # THIS RUNS EVERYTIME BEFORE ANY TEST.
    def setUp(self):
        self.newStudent = hash.Student(
            "Jandir", "Porta", "123456", "jandir_porta@hotmail.com", 34)

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

    def test_getEmail(self):
        testStudentEmail = self.newStudent.getEmail()
        expectedEmail = "jandir_porta@hotmail.com"
        self.assertIs(testStudentEmail, expectedEmail, "The emails dont match")

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
        self.newHash.Insert(self.newStudent)
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
        self.newHash.Insert(self.newStudent)
        self.assertTrue(self.newHash.Delete(self.newStudent))
        # CHECKING IF IT ACTUALLY DELETED THE STUDENT
        self.assertFalse(self.newHash.Exists(self.newStudent))

    def test_Delete_With_Non_Existing_Item(self):
        self.assertFalse(self.newHash.Delete(self.newStudent))


if __name__ == '__main__':
    unittest.main()
