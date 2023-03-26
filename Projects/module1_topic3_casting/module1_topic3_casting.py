"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 11
Topic: 3
Assignment: Casting
Date: 01/12/2023
Accept input, cast to integer, output result.
"""
def printOutput(number):
    print(f"You entered integer value {number}.")

userInput = input("Enter a number: ")
try:
    number = int(userInput)
    printOutput(number)
except:
    try:
        number = float(userInput)
        number = number//1 # floor divide by 1 to remove decimals.
        number = int(number)
        printOutput(number)
    except:
        print(f"'{userInput}' is not a number.")

# Input             Expected                               Actual
#   8          You entered integer value 8.          You entered integer value 8.
#   42.6       You entered integer value 42.         You entered integer value 42.
#   number     'number' is not a number.             'number' is not a number.