"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 2
Assignment: Derived Class
Date: 03/31/2023
"""
import Address

class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, addy=None):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self._last_name = lname
        self._first_name = fname
        self.set_address(addy)

    def __str__(self):
        result = self._last_name + ", " + self._first_name
        if self.address != None:
            result += f"\n{str(self.address)}"
        return result

    def set_address(self, address):
        if isinstance(address, Address.Address):
            self.address = address
        else:
            self.address = None

    def display(self):
        result = self._last_name + ", " + self._first_name
        if self.address != None:
            result += f"\n{str(self.address)}"
        return result