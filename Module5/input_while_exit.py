"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 5
Topic: 2
Assignment: Input Validation while Loops
Date: 02/7/2023
"""
num = 0
while(float(num) != -1):
    valid = False
    while(not valid):
        num = input("Enter a value 1 - 100(-1 to quit): ")
        #accept string of numbers with one '-' and one '.' and also between 1 and 100 or -1
        if num.replace(".", "", 1).replace("-", "", 1).isnumeric() and ((1 <= float(num) <= 100) or float(num) == -1):
            valid = True
        else:
            print(f"'{num}' is invalid")
    if(float(num) != -1):
        print(f"You entered {num}")
print("Goodbye")