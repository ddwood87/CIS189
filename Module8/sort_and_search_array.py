"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 8
Topic: 4
Assignment: Search and Sort Arrays
Date: 03/01/2023
"""
import array as arr

def push_high_to_front(a, i):
    if 0 <= i < len(a)-1 and a[i] <= a[i+1]:
            #swap places
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            push_high_to_front(a, i-1) 
            #loop this function until the previous item is greater than the current

def sort_array(a):
    i = 0
    for i in range(len(a)-1):
        #if a[i] < a[i+1]:
            push_high_to_front(a, i)
    #there is no return because this method changes the array object


def search_array(a, t):
    try:    
        return a.index(t)
    except ValueError:
        return -1

if __name__ == '__main__':
    numbers = [4.3, 56.4, 2.9, 24.6, 4.3, 22.7]
    array = arr.array('d', numbers)

    search_terms = [56.4, 5.3]
    for t in search_terms:
        index = search_array(array, t)
        if index == -1:
            print(f"{t} was not found.")
        else:
            print(f"{t} was found at index {index}")

    print(array)
    sort_array(array)
    print('Sort array')
    print(array)