"""
name.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class Hello(object):

    def __init__(self, l, f):
        self.last = l
        self.first = f

    def blah(self):
        print("My first name is", self.first)
        print("My last name is", self.last)


a = Hello('Doe', 'John')
a.blah()


