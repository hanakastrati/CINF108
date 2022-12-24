#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733

"""
Created on Wed Sep 21 19:22:13 2022

@author: hanakastrati
"""
#ask user purchase amount
purchase = input("Enter purchase amount (numbers only)")
amount = float(purchase)

#compute state tax (0.082)
#compute county tax (0.03)
stateTax = 0.082 * amount
countyTax = 0.03 * amount

#compute totals
totalTax = stateTax + countyTax
totalSale = amount + totalTax

#display purchase amount
print("purchase amount is: ", amount)

#display state tax
print("state sales tax is: ", stateTax)

#display county tax
print("county sales tax is: ", countyTax)

#display total tax
print("total tax is: ", totalTax)

#display total sale 
print("total cost of sale  is: ", totalSale)