#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:13:35 2022

@author: hanakastrati
"""
import random

def part1():
    housesList = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']
    print(housesList)


numbers1 = []
numbers2 = []

def part2():
    for item in numbers1:
        numbers2.append(item)

def part3():
    elements = 0

    while elements <= 100:
        num = str(random.randint(1, 1000))
        numbers1.append(num)
        elements = elements + 1

    #print(numbers1)

def main():
    part1()
    part3()
    part2()
    print(numbers2)

if __name__ == "__main__":
    main()


# The following code can all be done in the same python file:
#Part 1: Write a statement that creates a list with the following strings:
#'Gryffindor', 'Ravenclaw', 'Hufflepuff', and 'Slytherin'. Print out the contents of this list.
# Part2: Assume the list numbers1 has 100 elements, and numbers2 is an empty list.
#  Write code that copies the values in numbers1 to numbers2.
# Part3: Create a list with 100 elements and use the code you wrote in Part 2 to
# copy this list to another list. Then print out list that is the copy.
