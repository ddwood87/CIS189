"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 12
Topic: 2
Assignment: Custom Exceptions
Date: 04/05/2023
"""
import unittest
from customer_exceptions import (Customer, 
                                 InvalidCustomerIdException, 
                                 InvalidNameException, 
                                 InvalidPhoneNumberFormat)

class test_custom_exceptions(unittest.TestCase):
    def setUp(self):
        self.valid_customer_id = 1000
        self.valid_last_name = 'Last'
        self.valid_first_name = 'First'
        self.valid_phone_number = '515-222-4444'

        # set of test case
        self.invalid_customer_ids = {1, 999, 10000, '1000'}
        self.invalid_names = {2, 2.4, 'su2an'}
        self.invalid_phone_numbers = {'(515)555-3333', 5555555555, '5555555555'}

    def tearDown(self):
        del (self.valid_customer_id, 
             self.valid_last_name, 
             self.valid_first_name, 
             self.valid_phone_number,
             self.invalid_customer_ids,
             self.invalid_names,
             self.invalid_phone_numbers)

    def test_valid_customer(self):
        valid_customer = Customer(self.valid_customer_id,
                                  self.valid_last_name,
                                  self.valid_first_name,
                                  self.valid_phone_number)
        
        self.assertIsInstance(valid_customer, Customer)

    def test_invalid_customer_id(self):
        for id in self.invalid_customer_ids:
            with self.assertRaises(InvalidCustomerIdException):
                invalid_customer = Customer(id,
                                            self.valid_last_name,
                                            self.valid_first_name,
                                            self.valid_phone_number)

    def test_invalid_last_name(self):
        for name in self.invalid_names:
            with self.assertRaises(InvalidNameException):
                invalid_customer = Customer(self.valid_customer_id,
                                            name,
                                            self.valid_first_name,
                                            self.valid_phone_number)

    def test_invalid_first_name(self):
        for name in self.invalid_names:
            with self.assertRaises(InvalidNameException):
                invalid_customer = Customer(self.valid_customer_id,
                                            self.valid_last_name,
                                            name,
                                            self.valid_phone_number)
                
    def test_invalid_phone_number(self):
        for number in self.invalid_phone_numbers:
            with self.assertRaises(InvalidPhoneNumberFormat):
                invalid_customer = Customer(self.valid_customer_id,
                                            self.valid_last_name,
                                            self.valid_first_name,
                                            number)
                
if __name__ == '__main__':
    unittest.main()