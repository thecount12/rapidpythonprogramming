"""
kungfu1.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class KungFu(object):
    my_str = "The master"


class Master(KungFu):
    my_str = "Student is not the master"


teacher = Master.my_str
print(teacher)

