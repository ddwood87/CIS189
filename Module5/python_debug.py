"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 5
Topic: 4
Assignment: Debugging in Python
Date: 02/7/2023
"""
def print_to_number(number):
    """Prints to the number value passed in, beginning at 1"""
    # range() 'start' parameter is inclusive, but 'stop' parameter is exclusive of the parameter value
    # must add 1 to 'stop' parameter to include 'number'
    for counter in range(1,number+1):         
        print (counter)
if __name__ == "__main__":
    print_to_number(5)