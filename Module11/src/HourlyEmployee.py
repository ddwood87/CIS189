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

class HourlyEmployee(Employee):

    _hourly_pay: float
    _start_date: date

    def __init__(self, 
                 lname: str, 
                 fname: str, 
                 address: str, 
                 city: str,
                 state_code: str,
                 phone_number: str,
                 hourly_pay: float,
                 start_date: date):
        super().__init__(lname, fname, address, city, state_code, phone_number)
        self.set_hourly_pay(hourly_pay)
        self.set_start_date(start_date)

    def set_hourly_pay(self, rate):
        if 10 <= rate <= 20:
            self._hourly_pay = rate
        else:
            raise ValueError
        
    def give_raise(self, raise_amount):
        if 0 < raise_amount <= 4:
            self.set_hourly_pay(self._hourly_pay + raise_amount)
        else:
            raise ValueError

    def set_start_date(self, start_date):
        if isinstance(start_date, date):
            self._start_date = start_date
        else:
            raise ValueError

    def display(self):
        result = '----Hourly----\n'
        result += super().display()
        result += f'\nRate: ${self._hourly_pay}\nStart Date: {self._start_date}'
        return result
    
if __name__ == '__main__':
    new_hourly_employee = HourlyEmployee('Wood', 'Dominic', '323 W Brand St', 'Ames', 'IA', '515-333-4444', 10, date.today())
    print(new_hourly_employee.display())
    new_hourly_employee.give_raise(2)
    print(new_hourly_employee.display())