"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 7
Topic: 1
Assignment: Basic List
Date: 02/14/2023
"""

def make_list(num) -> list:
    count = 0
    result = list()
    while count < num:
        bad_input = True
        while bad_input:
            user_input = get_input().replace(',', '') #remove commas from input
            #remove one decimal. check for numeric.
            if user_input.replace('.', '', 1).isnumeric(): 
                result.append(float(user_input))
                bad_input = False
            else:
                print("Please enter a number.")
        count += 1
        
    return result
def get_input() -> str:
    return input("Enter a number:")

if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))