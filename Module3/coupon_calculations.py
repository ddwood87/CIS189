"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 3
Topic: 3
Assignment: Nested if statement
Date: 01/24/2023
"""
cashCoupons = [5, 10]
discountCoupons = [0.10, 0.15, 0.20]
salesTax = .06

userInput = input("Enter the cost of your order: ")
cost = 0
cashDiscount = 0
percentDiscount = 0

if userInput.replace(".", "", 1).isdecimal():
    cost = float(userInput)
    print("\nCash-Off Discounts")
    print("0. No Cash Coupon")                  #print option for no discount
    optionNumber = 1
    for c in cashCoupons:                       #print list of available discounts
        print(f"{optionNumber}. ${c} off")
        optionNumber += 1
    userInput = input("Choose a cash coupon amount option: ") #take user input
    if userInput.isdigit():
        ind = int(userInput) - 1                #index of selected coupon is optionNumber -1
        if -1 <= ind <= optionNumber - 1:       #check for valid option
            if ind == -1:                       #check for 'none' option
                cashDiscount = 0
            else:
                cashDiscount = cashCoupons[ind] #assign discount amount per selection
            print("\nPercent-Off Discounts")
            print("0. No Discount Coupon")      #print option for no discount
            optionNumber = 1
            for d in discountCoupons:           #print list of available coupons
                print(f"{optionNumber}. {(d * 100):.0f}%")
                optionNumber += 1
            userInput = input("Choose a discount coupon: ") #take user input
            if userInput.isdigit():              
                ind = int(userInput) - 1
                if -1 <= ind <= optionNumber - 1: #check for valid option
                    if ind == -1:                 #check for 'none' option
                        percentDiscount = 0
                    else:
                        percentDiscount = discountCoupons[ind] #assign discount per selection
                else:
                    print("Invalid Option")
            else:
                print("Invalid Entry")
        else:
            print("Invalid Option")
    else:
        print("Invalid Entry")
else:
    print("Invalid Cost")

#calculate discounts
discountCost = (cost - cashDiscount)
discountCost -= discountCost * percentDiscount

#calculate shipping
    #up to $10 dollars, shipping is $5.95
    #$10 and up to $30 dollars, shipping is $7.95
    #$30 and up to $50 dollars, shipping is $11.95
    #Shipping is free for $50 and over
shippingCost = 0
if discountCost < 10:
    shippingCost = 5.95
elif 10 <= discountCost < 30:
    shippingCost = 7.95
elif 30 <= discountCost < 50:
    shippingCost = 11.95

#calculate tax total and add shipping cost
total = discountCost * (1 + salesTax)
total += shippingCost

#transaction detail
print(f"\nSubtotal:         {cost:>8.2f}")
print(f"Cash off:         {(cashDiscount * -1):>8.2f}")
print(f"{(percentDiscount * 100):>2.0f}% discount:     {((discountCost * percentDiscount) * -1):>8.2f}")
print(f"Sales Tax ({(salesTax * 100):.0f}%):   {(discountCost * salesTax):>8.2f}")
print(f"Shipping:         {shippingCost:>8.2f}")
print(f"Total:           ${total:>8.2f}")