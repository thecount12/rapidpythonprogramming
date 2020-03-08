"""
repr.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


my_list = []
for i in range(1, 7):
    my_list.append(i)
blah = my_list
print(repr(my_list))
print(blah)
print(repr(blah))

