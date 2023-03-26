"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 9
Topic: 1
Assignment: Python Package import
Date: 03/07/2023
"""
# omit package name when driver is inside package
import greeting as gr
import dictionary_ops as do
import set_ops as so


if __name__ == "__main__":
    gr.greeting()
    dictionary = {
        'black': 'Night Sky',
        'red': 'Sunset Horizon',
        'blue': 'Clear Day'
    }
    do.print_dict(dictionary)
    test_set = {'Numbers', 'Books', 'Papers', 'Desks', 'Files'}
    so.print_set(test_set)
    gr.message()