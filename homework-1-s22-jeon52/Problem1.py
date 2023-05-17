#!/usr/bin/python3
import math
number = 100
# Your code should be below this line

# Check if the number is even and part of the Fibonacci Sequence
# not a negative number X
# even number (zero is positive and even) X
# (5n^2 + 4) or (5n^2 - 4) square roots are perfect numbers - check both 

if (number % 2 == 0) and (number >= 0): #check if number is even, and at least 0 
    if (math.sqrt(5 * (number ** 2) + 4) % 1) == 0: 
        print("Yes")
    elif (math.sqrt(5 * (number ** 2) - 4) % 1) == 0:
        print("Yes")
    else: #when both cases are not met
        print("No")
else: #not even or negative
    print("No")