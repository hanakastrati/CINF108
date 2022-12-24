#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Fri Oct 28 23:22:50 2022

@author: hanakastrati
"""

listInput = int(input("Enter your first number, negative number -> stops"))

big = listInput
small = listInput
total = 0
count = 0

while listInput >= 0:
    if listInput > big:
        big = listInput
    if listInput < small:
        small = listInput 
    count = count + 1
    print("count is" , count)
    total = total + listInput
    print("total is" , total)
 
    listInput = int(input("Enter your next number, negative number -> stops"))
    
average = total/count
print("largest integer is " , big)
print("smallest integer is " , small)
print("Average is " , average)


# Write a python program named computeAverage.py that reads in a list of nonnegative 
# integers and to display the largest integer, the smallest integer, and the average 
# of all the integers. The user indicates the end of the input by entering a negative 
# sentinel value that is not used in finding the largest, smallest, and average values. 
# The average should be a value of type double, so that it is computed with a fractional
#  part. Ex. user inputs the following:
# 10
# 2
# 50
# 100
# 1
# -1000 
# (note: The -1000 is an example of a sentinel value so we stop taking input from 
#  the user and we do not use the -1000 in our computation. Must do this for all 
#  negative numbers not just -1000)

# sample output:
# Largest integer is 100
# Smallest integer is 1
# Average of all the integers is 32.6


