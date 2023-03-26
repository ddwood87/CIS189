"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 5
Topic: 1
Assignment: Basic for Loops
Date: 02/7/2023
"""
numbers = [2.03, 4.66, 3.14, 9.5, 19.3]
i = 1
for x in numbers:
    print(f"Value {i}: {x}")
    i += 1
for x in reversed(range(33, 100)):
    print(x)