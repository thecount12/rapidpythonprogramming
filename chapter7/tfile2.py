"""
tfile2.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""

# lib
from tfile1 import *

mygen(my_list)

for x, y in zip([z for z in range(9)], mygen(my_list)):
    print(repr(x), repr(y))
for x, y in zip([z for z in range(9) if z > 5], mygen(my_list)):
    print(x)
print("__________________")
for x, y in zip([z for z in range(9) if z > 5], mygen(my_list)):
    print(y)
print("__________________")
for i in mygen(my_list):
    print(i)
print(list(mygen(my_list)))

