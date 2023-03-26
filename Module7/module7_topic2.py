"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 7
Topic: 2
Assignment: Function Keyword & Arbitrary Args
Date: 02/21/2023
"""

# I couldn't get the other average_scores method to reference
# this definition without changing the name.
def average_scores_(*args):
    sum = 0
    i = 0
    for a in args:
        sum += float(a)
        i += 1
    return sum / i 

if __name__ == '__main__':
    print(average_scores_(4, 3, 2, 4))
    print(average_scores_(4, 3, 2, 4, 1, 5))
    print(average_scores_(4.1, 3.4))


def average_scores(*args, **kwargs):
    # Use *args for average calculation
    # return
    result = "Result:"
    key_value = []
    for key, value in kwargs.items():
        result += f" {key} = {value}"
    result += f" with current average {average_scores_(*args)}"
    return result
    

if __name__ == '__main__':
    print(average_scores(72, 56, 84, 93, name='Dominic', 
                         gpa=3.4, course='Python!'))