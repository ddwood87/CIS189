"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 4
Assignment: Overriding Class Methods
Date: 04/02/2023
"""
from Employee import Employee
from datetime import date

class SalariedEmployee(Employee):

    _start_date: date
    _salary: int

    def __init__(self,  
                 lname: str, 
                 fname: str, 
                 address: str, 
                 city: str,
                 state_code: str,
                 phone_number: str,
                 salary: int,
                 start_date: date):
        super().__init__(lname, fname, address, city, state_code, phone_number)
        self.set_salary(salary)
        self.set_start_date(start_date)

    def set_salary(self, salary):
        if 30000 < salary < 70000:
            self._salary = salary
        else:
            raise ValueError
        
    def set_start_date(self, start_date):
        if isinstance(start_date, date):
            self._start_date = start_date
        else:
            raise ValueError
        
    def give_raise(self, raise_amount):
        if 1000 < raise_amount < 10000:
            self.set_salary(self._salary + raise_amount)
        else:
            raise ValueError
        
    def display(self):
        result = '----Salaried----\n'
        result += super().display()
        result += f'\nSalary: ${self._salary}\nStart Date: {self._start_date}'
        return result
    
if __name__ == '__main__':
    new_salaried_employee = SalariedEmployee('Wood', 'Dominic', '321 Center Ave', 'St. Charles', 'IA', '555-222-3333', 40000, date.today())
    print(new_salaried_employee.display())
    new_salaried_employee.give_raise(5000)
    print(new_salaried_employee.display())