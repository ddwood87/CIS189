"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 8
Topic: 3
Assignment: Selection using Dictionary
Date: 03/01/2023
"""

def switch_level(choice):
    level = {
        "N": 50,
        "B": 150,
        "E": 300,
        "A": 500
    }
    return level.get(choice)

def switch_level_name(choice):
    level = {
        "N": "Novice",
        "B": "Beginner",
        "E": "Experienced",
        "A": "Advanced"
    }
    return level.get(choice)

def main():
    levels = ['N', 'B', 'E', 'A']
    for l in levels:
        print(f"The new character is a(n) {switch_level_name(l)} and is awarded {switch_level(l)} points!")

if __name__ == '__main__':
    main()