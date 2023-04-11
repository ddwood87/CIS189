"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 12
Topic: 2
Assignment: Custom Exceptions
Date: 04/05/2023
"""
from json import dumps

class Customer:
    _customer_id: int
    _last_name: str
    _first_name: str
    _phone_number: str

    def __init__(self,
                 customer_id: int,
                 last_name: str,
                 first_name: str,
                 phone_number: str):
        self.set_customer_id(customer_id)
        self.set_last_name(last_name)
        self.set_first_name(first_name)
        self.set_phone_number(phone_number)

    def __str__(self):
        result = f'Customer Id: {self._customer_id}\n'
        result += f'Name: {self._first_name} {self._last_name}\n'
        result += f'Phone: {self._phone_number}'
        return result

    def __repr__(self):
        return dumps(self)
    
    def set_customer_id(self, customer_id):
        if (isinstance(customer_id, int) and
            1000 <= customer_id < 10000):
            self._customer_id = customer_id
        else:
            raise InvalidCustomerIdException

    def set_last_name(self, last_name: str):
        if isinstance(last_name, str) and last_name.isalpha():
            self._last_name = last_name
        else:
            raise InvalidNameException

    def set_first_name(self, first_name: str):
        if isinstance(first_name, str) and first_name.isalpha():
            self._first_name = first_name
        else:
            raise InvalidNameException
    
    def set_phone_number(self, phone_number: str):
        if isinstance(phone_number ,str) and phone_number.count('-') == 2:
            substrings = phone_number.split('-')
            if (len(substrings[0]) == 3 and
                len(substrings[1]) == 3 and
                len(substrings[2]) == 4 and
                phone_number.replace('-','').isnumeric()):
                self._phone_number = phone_number    
            else:
                raise InvalidPhoneNumberFormat
        else:
            raise InvalidPhoneNumberFormat

    def display(self):
        result = '----Customer----\n'
        result += str(self)
        result += '\n----------------'
        return result

class InvalidCustomerIdException(Exception):
    def __str__(self):
        return self.__class__.__name__

class InvalidNameException(Exception):
    def __str__(self):
        return self.__class__.__name__

class InvalidPhoneNumberFormat(Exception):
    def __str__(self):
        return self.__class__.__name__

if __name__ == '__main__':

    # This constructor call raises an exception when
    # setting the customer_id attribute.
    try:
        customer1 = Customer('4321',
                            'Brown',
                            'Carl',
                            '555-444-3333')
        print(customer1.display())
    except Exception as e:
        print(e)
        print('Customer 1 was not created.')
    
    # This constructor call raises an exception when
    # setting the last_name attribute
    try:
        customer2 = Customer(1234,
                            'Fr4nklin',
                            'Jen',
                            '555-555-5555')
        print(customer2.display())
    except Exception as e:
        print(e)
        print('Customer 2 was not created.')

    # This constructor call raises an exception when
    # setting the first_name attribute
    try:
        customer3 = Customer(1234,
                            'Franklin',
                            '6en',
                            '555-555-5555')
        print(customer3.display())
    except Exception as e:
        print(e)
        print('Customer 3 was not created.')

    # This constructor call raises an exception when
    # setting the first_name attribute
    try:
        customer4 = Customer(1234,
                            'Franklin',
                            'Jen',
                            '555555-5555')
        print(customer4.display())
    except Exception as e:
        print(e)
        print('Customer 4 was not created.')

    # Valid constructor call
    try:
        customer5 = Customer(1234,
                            'Franklin',
                            'Jen',
                            '555-555-5555')
        print(customer5.display())
    except Exception as e:
        print(e)
        print('Customer 5 was not created.')
    print(str(customer5))

    