"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 5
Assignment: Multiple Inheritance
Date: 04/02/2023
"""
from Employee import Employee
from HourlyEmployee import HourlyEmployee
from SalariedEmployee import SalariedEmployee
from Person import Person
from Address import Address
from datetime import date

class Manager(Person, SalariedEmployee):

    department: str
    direct_reports: list[Employee]

    def __init__(self, lname, fname, address, start_date, salary):
        #super().__init__(lname, fname, address)
        self.set_last_name(lname)
        self.set_first_name(fname)
        self.set_address(address)
        self.set_start_date(start_date)
        self.set_salary(salary)

    def display_direct_reports(self):
        result = ''
        result += f"\n{self._first_name} {self._last_name}'s direct reports:\n"
        for employee in self.direct_reports:
            result += employee.display() + '\n'
        return result
    
    def display(self):
        result = '----Manager----\n'
        result += super(Person, self).display()
        return result

if __name__ == '__main__':
    new_Address = Address('232', 'Center', 'Ave', 'Des Moines', 'IA', '50320')
    new_manager = Manager('Wood', 'Dominic', new_Address, date.today(), 40000)
    print(new_manager.display())

    employees = list[Employee]()
    for i in range(3):
        employees.append(HourlyEmployee(str(i), 'Employee', f'12{i} Baker St', 'Des Moines', 'IA', f'555-3{i}3-2222', 12.50+i , date.today()))
    new_manager.direct_reports = employees
    print(new_manager.display_direct_reports())
    new_manager.give_raise(2000)
    print(new_manager.display())
