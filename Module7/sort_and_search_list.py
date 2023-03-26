"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 7
Topic: 1
Assignment: Search and Sort List
Date: 02/20/2023
"""
import basic_list #requires basic_list.py in directory


def sort_list(l: list):
    l.sort()
    #sorts list passed to it, no return needed
    #I was surprised the list in main is altered 
    #by this without return and assignment

def search_list(list_):
    bad_input = True
    result = ""
    term = ""
    while bad_input:
        term = input("Enter number to search for: ").replace(',','')
        if term.replace('.', '', 1).isnumeric():
            bad_input = False
            if list_.__contains__(float(term)):
                result = list_.index(float(term))
        else:
            return "Please enter a decimal or integer number."
    if result == "":
        return "The search returned no result."
    else:
        return f"{term} was found at index {result}"
    #returns string describing search result
    

if __name__ == '__main__':
    num_list = basic_list.make_list(4)
    original = list(num_list)  #new list object
    sorted = num_list          #referential assignment
    sort_list(sorted)
    print(num_list)    #num_list is also sorted
    print(sorted)      #sorted and num_list refer 
                       #to the same list object

    print(original)    #creating a new list object
                       #retains the original order

    print(search_list(num_list))