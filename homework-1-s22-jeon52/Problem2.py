#!/usr/bin/python3
import math
n = 21
# Your code should be below this line

if n > 31 or n <= 0: #if not valid number
    print("Not valid")
elif n == 1 or n == 2 or n == 8 or n == 9 or n == 15 or n == 16 or n == 22 or n == 23 or n == 29 or n == 30:
    print("Weekend")
else: 
    print("Weekday")