"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 10
Topic: 3
Assignment: Unit Test a Class
Date: 03/25/2023
"""

class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        if (not isinstance(lname, str)
                or not isinstance(fname, str)
                or not isinstance(major, str)
                or not (isinstance(gpa, float) and 0 <= gpa <= 4)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


