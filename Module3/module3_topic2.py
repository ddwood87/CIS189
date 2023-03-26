"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 3
Topic: 2
Assignment: Compound Expressions
Date: 01/24/2023
"""
MAX = 10
MIN = 0
y = 12
print(f"y = {y}")
if y > MAX:
    print(f"y is more than maximum of {MAX}.")
if y < MIN:
    print(f"y is less than minimum of {MIN}.")
x = 3
print(f"x = {x}")
if MIN < x < MAX:
    print("x is more than minimum and less than maximum.")
if MIN <= x < MAX:
    print("x is more than or equal to minimum and less than maximum.")
if MIN <= x <= MAX:
    print("x is more than or equal to minimum and less than or equal to maximum.")