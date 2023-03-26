"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 10
Topic: 2
Assignment: Classes Practice
Date: 03/23/2023
"""
from json import dumps

class Customer:
    _customer_id: int
    _last_name: str
    _first_name: str
    _phone_number: str
    _address: str

    def __init__(self,
                 customer_id: int,
                 last_name: str,
                 first_name: str,
                 phone_number: str,
                 address: str):
        self.set_customer_id(customer_id)
        self._last_name = last_name
        self._first_name = first_name
        self._phone_number = phone_number
        self._address = address

    def __str__(self):
        result = f'Customer Id: {self._customer_id}\n'
        result += f'Name: {self._first_name} {self._last_name}\n'
        result += f'Phone: {self._phone_number}\n'
        result += f'Address: {self._address}'
        return result

    def __repr__(self):
        return dumps(self)
    
    def set_customer_id(self, customer_id):
        if isinstance(customer_id, int):
            self._customer_id = customer_id
        else:
            raise AttributeError("Customer Id must be an integer")

    def display(self):
        result = '----Customer----\n'
        result += str(self)
        result += '\n----------------'
        return result

if __name__ == '__main__':
    customer1 = Customer(1234,
                         'Franklin',
                         'Jen',
                         '555-555-5555',
                         '2122 2nd Street')
    print(customer1.display())

    # This constructor call raises an exception when
    # setting the customer_id attribute.
    customer2 = Customer('4321',
                         'Brown',
                         'Carl',
                         '555-444-3333',
                         '134 Broad Way')
    print(customer2.display())