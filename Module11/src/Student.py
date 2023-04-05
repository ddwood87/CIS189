"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 2
Assignment: Derived Class
Date: 03/31/2023
"""
from Person import Person
from Address import Address
from datetime import date

class Student(Person):

    def __init__(self,
                 student_id,
                 lname, 
                 fname,
                 major='Computer Science', 
                 gpa=0.0,
                 start_date = None,                   
                 addy=None
                 ):
        super().__init__(lname, fname, addy)
        self.avail_major = set({'English', 'CIS', 'History', 'Computer Science', 'Engineering'})
        self.student_id = student_id
        self.major = major
        self.start_date = start_date
        self.gpa = gpa

    def __str__(self):
        return f'Student ID: {self.student_id}\n{super().__str__()}\nStart: {self.start_date}\nMajor: {self.major}\nGPA: {self.gpa}'

    def __repr__(self):
        result = repr(self.person)
        result += 'major = self.major'

    def change_major(self, new_major):
        if new_major in self.avail_major:
            self.major = new_major

    def update_gpa(self, new_gpa):
        try:
            self.gpa = float(new_gpa)
        except Exception as e:
            print(e)

    def display(self):
        result = '----Student----'
        result += '\n' + str(self)
        return result
    
if __name__ == '__main__':
    new_address = Address('2325', 'Brook',  'St.', 'Des Moines', 'IA', '50315')
    #new_person = Person.Person('Dominic', 'Wood', new_address)
    new_student = Student('0100323209', 'Wood', 'Dominic', 'Computer Science', 3.6, date(2020, 9, 28), new_address)
    print(new_student.display())
    new_student.change_major('CIS')
    new_student.update_gpa(3.0)
    print(new_student.display())
    del new_student, new_address #, new_person

    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student