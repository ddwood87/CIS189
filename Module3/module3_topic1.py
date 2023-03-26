"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 3
Topic: 1
Assignment: if, else, elif statements
Date: 01/24/2023
"""

subscriptions = ["Platinum", "Gold", "Silver", "Bronze", "Free Trial"]  #Subscription level names
maxCost = 60                                                            #Cost of highest level
print("Welcome to the Programmer's Toolkit Monthly Subscription Box!")
print("Available subscriptions: ")
optionNumber = 1                                            #Incrementer to number choices.
for sub in subscriptions:                                   #For loop through subscription types
    print(f"{optionNumber}. {sub}")                 
    optionNumber += 1
userInput = input("Enter the number of your choice: ")

if userInput.isdigit():                                   #Check that input string is a digit
    optionInt = int(userInput)
    if 1 <= optionInt < optionNumber:                       #Check for valid input range
        i = optionInt - 1                                   #Adjust choice to index of subscription name
        cost = maxCost - 10*i                               #Set cost of subscription relative to choice
        if i == (len(subscriptions) - 1):              #Check for special case of free trial
            cost = 0                                            
        print(f"You selected {subscriptions[i]}, the cost is ${cost}.")
    else:
        print("You must enter a listed option.")
elif userInput.isalpha(): 
    print("You must enter a number.") 
elif userInput.isalnum():
    print("You must enter only a number.")