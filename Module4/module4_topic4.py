"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 4
Topic: 4
Assignment: Function Parameter and Return
Date: 01/31/2023
"""

def multiply_string(string: str, n: int) -> str:
    try:
        if n < 1:
            raise Exception
    except:
        return "Invalid multiplier."
    else:
        return string * n

print(multiply_string("Hello!", 6))
print(multiply_string("Nooo", -3))