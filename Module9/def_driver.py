"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 9
Topic: 1
Assignment: Python Module import
Date: 03/07/2023
"""

import my_definitions as md

if __name__ == "__main__":
    md.greeting()
    dictionary = {
        'black': 'Night Sky',
        'red': 'Sunset Horizon',
        'blue': 'Clear Day'
    }
    md.print_dict(dictionary)
    test_set = {'Numbers', 'Books', 'Papers', 'Desks', 'Files'}
    md.print_set(test_set)
    md.message()