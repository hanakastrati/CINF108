#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Tue Dec  6 11:52:06 2022

@author: hanakastrati
"""


#open file has to be done outside everything
newFile = open("random.txt", 'w')  # open/create new file

def randNumGenerator():  # function that generates the number & writes it to the file
    #random number generator (range 1 - 800)
    num = str(random.randint(1, 800))
    #testing>>>
    print(num)
    #writes number into file
    newFile.write(num + '\n')

def main():  # main function that calls other functions

    #user input - how many numbers to generate
    howMany = int(input(
        "how many numbers do you want to generate? (enter a number greater than 0)"))

    #if wrong input is given, tells user to correct their input & asks how many again
    if howMany <= 0:
        print("your number has to be greater than 0")
        howMany = int(input(
            "how many numbers do you want to generate? (enter a number greater than 0)"))

    #helper variable for while loop
    count = howMany

    #while loop calls generator function & iterates as long as count > 0
    while count > 0:
        randNumGenerator()
        count = count - 1
    newFile.close()


#calls main
if __name__ == "__main__":
    main()
