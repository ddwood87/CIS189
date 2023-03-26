"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 4
Topic: 2 & 3
Assignment: Basic Functions
Date: 01/31/2023
"""

"""Returns a string after taking user input about name, hours, and pay rate"""
def hourly_employee_input() -> str:
    name  = input("\nEnter the employee's name: ").capitalize()
    result = "Invalid Entry"
    try:
        hours = int(float(input(f"Enter the hours worked by {name}: ")))
        if hours < 0:
            raise Exception
    except:
        print("Hours entered must be a positive whole number.")
    else:
        try:
            rate = float(input(f"Enter the hourly rate of {name}: "))
            if rate < 0:
                raise Exception
        except:
            print("Hourly rate must be a positive number.")
        else:
            result = f"{name} has worked {hours} hours at ${rate:.2f} per hour.\n"
            result += f"Total earned: ${hours * rate:.2f}"
    finally:
        return result

message = hourly_employee_input()
print(message)

message = hourly_employee_input()
print(message)

message = hourly_employee_input()
print(message)