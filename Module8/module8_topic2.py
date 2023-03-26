"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 8
Topic: 2
Assignment: Dictionary Update
Date: 02/28/2023
"""

def get_test_scores():
    scores_dict = dict()
    loop = True
    while loop:
        num_scores = input("Enter the number of test scores to enter: ")
        if num_scores.isnumeric():
            num_scores = int(num_scores)
            if 1 <= num_scores <= 10:
                loop = False
            else:
                print("Enter a number between 1 and 10")
        else:
            print("Enter the number of tests.")
    print(f'\nEnter test scores: ')
    for i in range(1, num_scores + 1):
        loop = True
        while loop:
            in_str = input(f"{i}: ")
            if len(in_str) > 0:
                in_str = in_str.replace(",","")
                if in_str.replace(".","",1).isnumeric():
                    scores_dict.update({i:float(in_str)})   #update with key of i
                    loop = False        #Exit while loop condition
                else:
                    print("Enter a decimal number.")
            else:
                print("Please enter a test score.")
    return scores_dict

def average_scores(score_dict):
    if len(score_dict) < 1:
        raise ValueError("Empty dictionary cannot be averaged.")
    return sum(score_dict.values())/len(score_dict)

if __name__ == '__main__':
    print(f"Average score: {average_scores(get_test_scores())}")