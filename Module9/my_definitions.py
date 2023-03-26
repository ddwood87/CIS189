"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 9
Topic: 1
Assignment: Python Module
Date: 03/07/2023
"""

def greeting():
    print('Hello, user!')

def message():
    print('This code was written by Dominic Wood')

def print_dict(dictionary: dict):
    for key in dictionary.keys():
        print(f'{key}, {dictionary[key]}')

def print_set(set: set):
    for s in set:
        print(s)