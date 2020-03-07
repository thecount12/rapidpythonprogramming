"""
arg2.py
Chapter 3 input
Author: William C. Gunnells
Rapid Python Programming
"""


import sys

if len(sys.argv) > 1:
    print("Number of arguments:", len(sys.argv)-1)
    for i in sys.argv[1:]:
        print(i)
else:
    print("no arguments...")


