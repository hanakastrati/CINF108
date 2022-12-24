#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Fri Dec  9 22:45:56 2022

@author: hanakastrati
"""

def convert_mysteryUnit_to_specialUnits(mysteryUnits):
    specialUnits = 27 * mysteryUnits
    return specialUnits

def main():
    howMany = int(input("how many mysteryUnits are we converting"))
    while howMany > 0:
        mysteryUnits = int(input("enter your mysteryUnit"))
        newConversion = convert_mysteryUnit_to_specialUnits(mysteryUnits)
        howMany = howMany - 1
        print(newConversion)

#calls main
if __name__ == "__main__":
    main()

# One mysteryUnit equals to 27 specialUnits.
# Write a function named convert_ mysteryUnit _to_ specialUnits that accepts a
# number of mysteryUnits as an argument and returns the number of specialUnits
# in that many mysteryUnits. Use the function in a program that prompts the user
# for how many numbers they would like to convert and then to enter a number of
# mysteryUnits. Then display the number of specialUnits in that many mysteryUnits
#  for each number entered by the user. (Expected Functions: convert_mysteryUnit
#                                        _to_ specialUnits and main).