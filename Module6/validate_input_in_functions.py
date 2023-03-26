"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 6
Topic: 1
Assignment: Functions Default Values
Date: 02/14/2023
"""

#score input function
#params: test_name, test_score, invalid_message
#returns string test name and (score or invalid message)
def score_input(test_name, test_score = -1, invalid_message = 'Invalid test score!') -> str:
    def error():
        return test_name + ": " + invalid_message
    def success():
        return test_name + ": " + "{:0g}".format(test_score)
    try:
        test_score = float(test_score)
    except:
        invalid_message = 'ValueError encountered!'
        return error()
    if(test_score < 0):
        invalid_message += ' You must enter a positive score.'
        return error()
    elif(0 <= test_score <= 100):
        return success()
    return error()        #error if score fits no test cases
    
display_string = score_input('Test 1', 70
                             )
print(display_string)
display_string = score_input('Test 2', invalid_message='No score input.')             #uses -1 default score value
print(display_string)
display_string = score_input('Test 3', 100.001)
print(display_string)
display_string = score_input('Test 4', 'dog')
print(display_string)