"""
lam.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


def blah(item):
    return (lambda x: x * x)(item)


print(blah(2))

