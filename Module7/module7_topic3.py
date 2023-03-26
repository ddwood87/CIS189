"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 7
Topic: 3
Assignment: File I/O using Tuples
Date: 02/21/2023
"""
import os as os

def write_to_file(*args):
    name = args[0]
    scores = args[1]
    write_string = f'{name}, ' + ', '.join(map(str, scores))
    with open('student_info.txt', 'a') as file:
        file.write(write_string + '\n')

def get_student_info(name):
    print(f'\nEnter test scores for {name}: ')
    print("Enter 'no' to stop.")
    loop = True
    i = 1
    scores = []
    while loop:
        in_str = input(f"{i}: ")
        if len(in_str) > 0:
            in_str = in_str.replace(",","")
            if in_str.replace(".","",1).isnumeric():
                scores.append(float(in_str))
                i += 1
            elif in_str[0] in ('n', 'N'):   #if input string contains n,
                loop = False        #Exit while loop condition
                print(f"Scores entered for {name}: {', '.join(str(s) for s in scores)}")
            else:
                print("Enter a decimal number.")
        else:
            print("Please enter a test score.")
    info = name, scores
    write_to_file(*info) 

def read_from_file():
    file_dir = os.path.dirname(__file__)
    file_name = 'student_info.txt'
    print(f"\n'{file_name}' file contents")
    with open(os.path.join(file_dir, file_name), 'r') as file:
        print(file.read())

def delete_file():
    os.remove('student_info.txt')

if __name__=='__main__':

    get_student_info('Brandon')
    get_student_info('Troy')
    get_student_info('Alex')
    get_student_info('Mary')

    read_from_file()
    delete_file()
    

"""
Item
File I/O using Tuples Assignment
File I/O using Tuples Assignment
What you're creating
In this assignment you will tie together the seemingly unrelated tuple and arbitrary argument list to perform file input and output.  Your program will take a student's name and an unknown number of test scores, store them in a tuple, save that tuple into a file, and then finally print the data from the file back to the screen.
How you're doing it

    Write a function write_to_file() that accepts a tuple to be added to the end of a file
        Open the file for appending (name your file 'student_info.txt')
        Write the tuple on one line (include any newline characters necessary)
        Close the file
    Write a function get_student_info() that 
        Accepts an argument for a student name
        Prompts the user to input as many test scores as they wish
        Stores the information (name and scores) in a tuple
        Calls the function write_to_file() sending the tuple to be written to the end of the file
    Write a function read_from_file() that
        Reads a file line by line
        Prints each line to the console
    In main
        Call the get_student_info() for at least 4 different students.
        Call read_from_file()

Notes/Hints

    Because tuples are immutable, you'll want to store your data in a tuple that has a list nested inside of it.
        ('name',[score1,score2,score3,etc.])
        You'll be able to edit the list inside the tuple.  In the example above, you could append to the list by doing something like this:  score_list[1].append(student_score)
    There are more elegent ways to do things but for this assignment, you can just write the tuples to the file as strings and then read the strings back at the end of the program
    Remember that you'll also need to include a "\n" to each line you write to the file so you don't just end up with one long string on a single line
    Because you are going to be appending to the file each time, it might be good for you to include this as the first thing you do in your main:
        open("student_info.txt","w").close()
        It basically overwrites the file with a blank file.
        This prevents you from appending more and more each time you rerun your program.

Submit your working .py file.  This is worth 10 points.
"""