"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 10
Topic: 3
Assignment: Unit Test a Class
Date: 03/25/2023
"""
import unittest
# I struggled to get python to recognize imports from other packages,
# but gave up and put this test class in the same package as the tested class
from Student import Student as s

class Test_Student(unittest.TestCase):
    def setUp(self):
        self.req_param_student = s('Smith', 'Joe', 'Engineering')
        self.all_param_student = s("Brown", "Paul", "History", 3.4)
    def tearDown(self):
        del self.req_param_student
        del self.all_param_student

    def test_object_created_required_attributes(self):

        #Test constructor values set to only required attributes for acceptable values
        self.assertEqual(self.req_param_student.last_name, "Smith")
        self.assertEqual(self.req_param_student.first_name, "Joe")
        self.assertEqual(self.req_param_student.major, "Engineering")
        self.assertEqual(self.req_param_student.gpa, 0)

    def test_object_created_all_attributes(self):

        #Test constructor values set to all attributes for acceptable values
        self.assertEqual(self.all_param_student.last_name, "Brown")
        self.assertEqual(self.all_param_student.first_name, "Paul")
        self.assertEqual(self.all_param_student.major, "History")
        self.assertEqual(self.all_param_student.gpa, 3.4)

    def test_student_str(self):

        #Test the str() method
        actual = str(self.all_param_student)
        expected = "Brown, Paul has major History with gpa: 3.4"
        self.assertEqual(actual, expected)

    def test_object_not_created_error_last_name(self):

        #that expected exception raised
        #Add exception to constructor (not in test!)
        with self.assertRaises(ValueError):
            student = s(2, 'Joe', 'Engineering')
        
    def test_object_not_created_error_first_name(self):
            
        #Add exception to constructor (not in test!)
        with self.assertRaises(ValueError):
            student = s('Smith', 2, 'Engineering')
        
    def test_object_not_created_error_major(self):

        #Add exception to constructor
        with self.assertRaises(ValueError):
            student = s('Smith', 'Joe', 2)

    def test_object_not_created_error_gpa(self):
        
        #Add exception to constructor
        #NOTE: look up how isinstance(gpa, float) works AND check range
        with self.assertRaises(ValueError):
            student = s('Smith', 'Joe', 'Engineering', 'Great')

if __name__ == '__main__':
    unittest.main()

