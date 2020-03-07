"""
kungfu1.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class KungFu(object):
    my_str = "The master"

    def crane(self):
        print("crane kick")


class Master(KungFu):
    my_str = "Student is not the master"

    def crane(self):
        print("must learn crane kick")


teacher = Master()
teacher.crane()
