#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Tue Nov 29 11:16:17 2022

@author: hanakastrati
"""
def is_prime(num):
    count = 0
    seq = range(1, (num +1) , 1)
    
    print(seq)
    
    for n in seq:
        if num % n == 0:
            count = count + 1
            print("n value in seq is", n, "count is", count)
    
    if count > 2:
        print("your number" , num , "is composite")
        return False
    else:
        print("your number" , num , "is prime")
        return True
