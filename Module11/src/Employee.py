"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 4
Assignment: Overriding Class Methods
Date: 04/02/2023
"""
from datetime import date
from json import dumps, loads

class Employee:
    '''Employee Class '''
    _last_name: str
    _first_name: str
    _address: str
    _city: str
    _state_code: str
    _phone_number: str

    # Constructor
    def __init__(self, 
                 lname: str, 
                 fname: str, 
                 address: str, 
                 city: str,
                 state_code: str,
                 phone_number: str):
        self.set_last_name(lname)
        self.set_first_name(fname)
        self.set_address(address)
        self.set_city(city)
        self.set_state_code(state_code)
        self.set_phone_number(phone_number)

    def __str__(self) -> str:
        result = f"{self._first_name} {self._last_name}\n"
        result += self._address + "\n"
        result += f"{self._city}, {self._state_code}"
        return result
    
    def __repr__(self) -> str:

        dictionary = self.__dict__
        dictionary['_class_name'] = self.__class__.__name__
        self_json = dumps(dictionary)
        return self_json
    
    def set_last_name(self, lname: str):
        self._last_name = lname

    def set_first_name(self, fname: str):
        self._first_name = fname

    def set_address(self, address: str):
        self._address = address

    def set_city(self, city: str):
        self._city = city

    def set_state_code(self, state_code: str):
        state_code = state_code.upper()
        if state_code.isalnum() and len(state_code) == 2:
            self._state_code = state_code
        else:
            raise ValueError

    def set_phone_number(self, phone_number: str):
        phone_number = phone_number.replace("(", "", 1).replace(")", "", 1).replace("-", "", 2)
        if phone_number[0] == '1':
            phone_number = phone_number[1::1] #drop leading 1
        if len(phone_number) == 10 and phone_number.isnumeric():
            self._phone_number = phone_number
        else:
            raise ValueError

    def display(self) -> str:
        result = '----Employee----\n'
        result += str(self)
        return result

if __name__ == '__main__':
    # Driver
    try:
        emp = Employee('Ruiz',
                    'Matthew',
                    '1515 Waffle Ave',
                    'Clarence',
                    'MO',
                    '(555)222-4444')   # call the constructor, needs to have a first and last name in parameter
        emp.set_first_name('Matt')
        print(emp.display())                # display returns a str, so print the information
        print(repr(emp))
        del emp                             # clean up!
    except ValueError:
        print('Error: The employee was not created')    

    try:
        emp = Employee('Wallace',
                    'Aaron',
                    '325 Plain Ave',
                    'Centerville',
                    'IN',
                    '(555)222-4444')   # call the construtor, needs to have a first and last name in parameter
        emp.set_first_name('Matt')
        print(emp.display())                # display returns a str, so print the information
        print(repr(emp))
        del emp                             # clean up!
    except ValueError:
        print('Error: The employee was not created')                  