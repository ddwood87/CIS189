"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 6
Topic: 2
Assignment: Inner Functions
Date: 02/14/2023
"""

def measurements(measures):
    def area(a_list):
        if(len(a_list) == 2):
            return a_list[0] * a_list[1]
        elif(len(a_list) == 1):
            return a_list[0] ** 2
        
    def perimeter(a_list):
        if(len(a_list) == 2):
            return 2 * (a_list[0] + a_list[1])
        elif(len(a_list) == 1):
            return a_list[0] * 4     
               
    return f'Perimeter = {perimeter(measures):0g} Area = {area(measures):0g}'

if __name__=='__main__':
    rectangle = [2.1, 3.4]
    result = measurements(rectangle)
    print(result)
    square = [3.5]
    result = measurements(square)
    print(result)