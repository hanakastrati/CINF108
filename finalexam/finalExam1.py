#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Fri Dec  9 22:14:40 2022

@author: hanakastrati
"""
import random

#open a new file & be able to write to the file
newFile = open("random.txt", 'w')

def random_generator(start, end):  # function that generates a random number
    #random number generator (range: start - end)
    num = random.randint(start, end)
    #testing>>>
    print("your randomly generated number is" , num)
    return num

def is_odd(number):
    if number % 2 :
        return False #even
    else:
        return True #false

def main():
    #range(start, stop, step)
    seq = range(1, 12, 1)

    print(seq)

    for n in seq:
        newNum = random_generator(1, 175)
        #print(newNum)
        odd = is_odd(newNum)
        #print(odd)
        if odd == False:
            print("your number" , newNum , "is even")
            newFile.write("your number" + str(newNum) + "is even")
        else:
            print("your number", newNum, "is odd")
            newFile.write("your number" + str(newNum) + "is odd")

#calls main
if __name__ == "__main__":
    main()


# Write a Python program that has three functions:
# • random_generator(start, end): returns a random number between two numbers, start and end.

# • is_odd(number): takes a number and checks if the number is even or odd. Returns true if it is odd, otherwise returns false. You must write your own code no built in functions can be used.

# • main(): creates a for loop that generates 12 random numbers between 1 and 175 by calling random_generator function, then calls the is_odd function to check if the random number is even or odd. Prints out if the number is even or odd by printing the number and even/odd information. Writes out to a file randomNumbers.txt what the number is and if the number is even or odd.
# Calls the main() function at the end.