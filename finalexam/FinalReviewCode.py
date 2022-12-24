#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Tue Nov 29 13:37:11 2022

@author: hanakastrati
"""
def find_min_max():
    numbersInputted = int(input("what is your number?"))
    min = numbersInputted
    max = numbersInputted
    
    moreInput = input("do you have more numbers to enter? (yes/no)")
    
    while (moreInput == "yes"):
        numbersInputted = int(input("what is your number?"))
        if(numbersInputted < min):
            min = numbersInputted
        if(numbersInputted > max):
            max = numbersInputted
        moreInput = input("do you have more numbers to enter? (yes/no)")        
    return min, max

def main():
    minValue, maxValue = find_min_max()
    print("min is",minValue)
    print("max is",maxValue)
    
if __name__ == "__main__":
    main()