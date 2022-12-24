#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 18:25:48 2022

@author: hanakastrati
"""

shapeOneLength = float(input("What is your shape one length."))
shapeOneWidth = float(input("What is your shape one width."))
shapeTwoLength = float(input("What is your shape two length."))
shapeTwoWidth = float(input("What is your shape two width."))

areaOne = [(shapeOneLength * shapeOneWidth * shapeOneLength * shapeOneWidth)/3]
print(areaOne)
areaTwo = [(shapeTwoLength * shapeTwoWidth * shapeTwoLength * shapeTwoWidth)/3]
print(areaTwo)

if areaOne > areaTwo:
    print("area of mystery shape one is greater than area of mystery shape two")
elif areaOne == areaTwo:
    print("area of mystery shape one is equal to the area of mystery shape two")
elif areaOne < areaTwo:
    print("area of mystery shape one is less than area of mystery shape two")