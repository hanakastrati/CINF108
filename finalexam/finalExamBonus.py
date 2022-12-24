#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Fri Dec  9 23:11:01 2022

@author: hanakastrati
"""
def area_of_shape1(base, height):
    shape1Area = (base * height)/4
    print("the area of shape 1 is" , shape1Area)
    return shape1Area

def area_shape2(base, height):
    shape2Area = base * height
    print("the area of shape 2 is" , shape2Area)
    return shape2Area

def volume_of_shape2s(base, height):
    area_of_shape2 = area_shape2(base, height)
    volume = area_of_shape2 * base
    #print("the area of shape 2 is" , area_of_shape2)
    #print("the volume of shape 2 is" , volume)
    return(volume)

def main():
    base = int(input("what is the base?"))
    height = int(input("what is the height?"))
    print("the volume of shape 2 is" , volume_of_shape2s(base, height))

#calls main
if __name__ == "__main__":
    main()

# Bonus Question: Write a Python program that calculates the volume of a shape2 by using the following functions:
# • area_of_shape1: Takes base and height as arguments and calculates/returns the area of a triangle: ( base ∗ height ) / 4 .
# • volume_of_shape2: takes base and height as arguments and calculates/returns the vol ume of a shape2: area_of_shape2  ∗ base
# • main: Takes base and height from the user and calculates the volume of a shape2 by calling the function volume_of_shape2