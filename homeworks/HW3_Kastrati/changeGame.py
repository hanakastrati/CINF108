#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733

"""
Created on Wed Oct  5 19:14:58 2022

@author: hanakastrati
"""

#ask user for amount of pennies
pennies = float(input("Enter number of pennies (numbers only)"))
penniesTotal = float(pennies*0.01)

#ask user for amount of nickles
nickles = float(input("Enter number of nickles (numbers only)"))
nicklesTotal = float(nickles*0.05)

#ask user for amount of dimes
dimes = float(input("Enter number of dimes (numbers only)"))
dimesTotal = float(dimes*0.10)

#ask user for amount of quarters
quarters = float(input("Enter number of quarters (numbers only)"))
quartersTotal = float(quarters*0.25)

coinsTotal = (penniesTotal + nicklesTotal + dimesTotal + quartersTotal)

if coinsTotal == 1.00:
    print("Congratulatiions, you win!")
elif coinsTotal > 1.00:
    print("You entered " , coinsTotal , ", which is more than 1.00")
elif coinsTotal < 1.00:
    print("You entered " , coinsTotal , ", which is less than 1.00")
    