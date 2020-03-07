"""
functionarg-input.py
Chapter 3 input
Author: William C. Gunnells
Rapid Python Programming
"""


def table_leaf(a, b=5):
    print("area of table:", a * b)


x = int(input("enter a number: "))
table_leaf(x)

