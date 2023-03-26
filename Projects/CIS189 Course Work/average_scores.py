"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 4
Topic: 1
Assignment: Basic Input and Output
Date: 01/31/2023
"""

def avg(score_list):
    return sum(score_list) / len(score_list)

score_count = 3
try:
    last_name = input("Enter your last name: ").lower().capitalize()
except:
    print("That didn't work.")
    last_name = "Unknown"
try:
    first_name = input("Enter your first name: ").lower().capitalize()
except:
    print("That didn't work.")
    last_name = "Unknown"
try:
    age = int(float(input("Enter your age (years): ")))
    if age < 18:
        raise Exception
except:
    print("You must enter an age, 18 or greater.")
    age = 0
scores = []
for i in range(1, score_count+1):
    try:
        s = float(input(f"Enter score #{i}: "))
        if 0 <= s <= 110:
            scores.append(s)
        else:
            raise Exception
    except:
        print("You must enter a score. (0-110)")
score_avg = avg(scores)
print(f"{last_name}, {first_name} age: {age} average grade: {score_avg}")
