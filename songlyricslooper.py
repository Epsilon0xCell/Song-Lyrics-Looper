# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:12:13 2023

@author: cy83r-3x71nc710n
"""

# Setting variables
    
repeat1 = 0
repeat2 = 0

# Counting up chorus

# Sets countup to value of range operation.
countup = range(3, 31, 3)

# While loop that checks if repeat1 is less than 2 and if it is continue the program

while repeat1 < 2:
# Create a for loop that goes through the countup list assigning x as each item in the list
    for x in countup:
        print(x,end=" ")
    print("\n")
    repeat1 = repeat1+1

# Counting down multiplication chorus


# Sets countdown to value of range operation.
countdown = range(10, 1, -1)


# Create a for loop that goes through the countdown list assigning y as each item in the list
for y in countdown:
 mult = 3*y
 print("\n \n 3 times" + " " + str(y) + " is" + " " + str(mult))             
print("\n \n 3 times 1 is 3 of course \n")
print("\n")

# While loop that checks if repeat1 is less than 2 and if it is continue the program

while repeat2 < 2:
# Create a for loop that goes through the countup list assigning x as each item in the list
    for x in countup:
        print(x,end=" ")
    print("\n")
    repeat2 = repeat2+1

