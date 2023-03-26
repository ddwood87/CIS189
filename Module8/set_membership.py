"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 8
Topic: 1
Assignment: Set
Date: 02/28/2023
"""

def in_set(object, set) -> bool:
    return object in set

if __name__ == "__main__":
    test_set = set([45, 40, 20, 19])
    test_value = 45
    is_in_set = in_set(test_value, test_set)
    print(f"The value '{test_value}' is {'' if is_in_set else 'not '}in the set {test_set}")