"""
introspect.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class MyObject(object):
    """
    a b c
    """

    def __init__(self):
        pass

    def cool(self):
        print("should print cool")


o = MyObject()

print(isinstance(o, MyObject))
print(isinstance(o, object))
print(isinstance(2, int))
print(isinstance('str', str))
print("===========")
print(hasattr(o, '__doc__'))
print(hasattr(object, '__doc__'))
print(hasattr(o.cool(), '__call__'))
print("------------")
print(getattr(o, '__doc__'))
print("=============")
print(getattr(object, '__doc__'))