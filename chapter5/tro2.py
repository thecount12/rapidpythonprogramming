"""
tro2.py
Chapter 5 Exceptions
Author: William C. Gunnells
Rapid Python Programming
"""


try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print("You did not enter a number")
