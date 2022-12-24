#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Tue Nov 29 10:46:36 2022

@author: hanakastrati
"""
newInput = int(input("please enter a positive integer"))
usable = newInput * 2
seq = range(1, usable, 2)

total = 0

for n in seq:
    total = total + n
    print(n)
    
print("The sum of the first" , usable , "positive odd integers is" , total)



# Part 2:
# Write a python program named oddSum.py that will compute the sum of the first n
# positive odd integers using a for loop (note range function may be useful here).
#  For example, if n is 5, you should compute 1 + 3 + 5 + 7 + 9. So in this case 
#  25 should be outputted. Your code must work for any positive number that is 
#  inputted. 
 
# sample user interaction:
 
# Please enter a positive integer:
# 5
# The sum of the first 5 possitive odd integers is 25.
