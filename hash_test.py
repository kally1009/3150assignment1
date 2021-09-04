import unittest
import hash
#from hash import Student
#from hash import Hash
#from hash import isPrime


class TestStudent(unittest.TestCase):
    # THIS RUNS EVERYTIME BEFORE ANY TEST.
    def setUp(self):
        self.newStudent = hash.Student(
            "Jandir", "Porta", "123456", "jandir_porta@hotmail.com", 34)

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
        self.assertIs(testStudentEmail, expectedEmail,
                      "The email do not match")

    def test_getAge(self):
        testStudentAge = self.newStudent.getAge()
        expectedAge = 34
        self.assertEqual(testStudentAge, expectedAge, "Both ages do not match")

    def test_eq(self):
        pass
        # How do I test these kinds of functions with overriding what == , >, <, and int?

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
        # does it return none when it doesn't exist?
        # return value... Look up what

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
