#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 17:55:24 2022

@author: hanakastrati
"""

stringInput = input("please enter a word") 
pile = "" 
for letter in [stringInput]: 
    pile = pile + letter 
    print(letter + 3)
print(pile)



fruitInput = input("What is your favorite fruit?")
if fruitInput == "apple":
    print("This is my favorite fruit too!")
else:
    print("My favorite fruit is different.")
    
    
    
shapeOneLength = input("What is your shape one length.")
shapeOneWidth = input("What is your shape one width.")
shapeTwoLength = input("What is your shape two length.")
shapeTwoWidth = input("What is your shape two width.")

areaOne = [(shapeOneLength * shapeOneWidth)^2 / 3]
areaTwo = [(shapeTwoLength * shapeTwoWidth)^2 / 3]

if areaOne > areaTwo:
    print("area of mystery shape one is greater than area of mystery shape two")
elif areaOne == areaTwo:
    print("area of mystery shape one is equal to the area of mystery shape two")
elif areaOne < areaTwo:
    print("area of mystery shape one is less than area of mystery shape two")