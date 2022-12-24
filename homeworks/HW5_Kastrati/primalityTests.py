#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Tue Dec  6 11:35:09 2022

@author: hanakastrati
"""
import primeNumbers

howMany = int(input("how many numbers do you want to test for primality? (enter a number)"))
count = howMany

while count > 0:
    num = int(input("what is your number? (enter a number)"))
    count = count - 1
    primeNumbers.is_prime(num)
