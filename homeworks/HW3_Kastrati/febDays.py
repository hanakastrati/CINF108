#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Wed Oct  5 19:39:06 2022

@author: hanakastrati
"""
year = int(input("What year?"))
days = int 

if year%100 == 0:
    if year%400 == 0:
        days = 29
elif year%100 != 0:
    if year%4 == 0:
        days = 29   
    else:
        days = 28

print(f"In the year {year}, February has {days} days.")