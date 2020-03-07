"""
unknown.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class Bar(object):

    def blah(self):
        print("cool")

    def strange(self):
        print("wow")

    def nice(self):
        print("very cool now")

    def bazinga(self):
        print("bazinga")


class Foo(Bar):

    def __iter__(self):  # iterate unknown
        return iter(vars(Bar))  # vars built-in attr


a = Foo()
for i in a: 
    print(i)
