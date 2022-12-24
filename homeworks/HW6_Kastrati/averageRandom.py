#Hana Kastrati
#Student ID: 001380226
#Course: CINF 108
#Section 8733
"""
Created on Fri Dec  9 04:33:26 2022

@author: hanakastrati
"""
import statistics

#to-do
#read in random.txt file
#calculate average
#calculate min
#calculate max
#calculate median
#calculate mode

# newFile = open("random.txt" , 'r')
# newList = []
# for line in newFile:
#     print(line)
#     line.rstrip("")
#     newList = newList + line
#     print("newList is" , newList)


#open & read text file
newFile = open("random.txt" , 'r')
count = 0

newList = []
line = newFile.readline()

big = int(line)
small = int(line)
total = 0

while line != '':
    count = count + 1
    newList = newList + [line]
    print(type(line))
    print("newList is" , newList)
    print("line" , count , "has the following value" , line)
    line = newFile.readline()
intList = [eval(i) for i in newList]


for i in intList:
    print(i)
    if  i > big:
        big = i
    if i < small:
        small = i
    total = total + i

average = total/count

print("total is" , total)
print("max is " , big)
print("min is " , small)
print("Average is " , average)
print("median is" , statistics.median(intList))
print("mode is" , statistics.mode(intList))





    # if (str(line) == ''):
    #     print("in if")
    #     line = newFile.readline()
    # else:
    #     print("in else")
    #     line = newFile.readline()




#calculate average
# length = len(newList)
# print("length is" , length)
# totalSum = 10
# print("sum is" , totalSum)
# def average():
#     average = totalSum / length
#     print("average is" , average)


# average()
