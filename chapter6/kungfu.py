"""
kungfu.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class KungFu(object):

    my_str = "The master"
    pass


class Master(KungFu):
    pass


teacher = Master.my_str
print(teacher)

