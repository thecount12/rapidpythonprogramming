"""
in.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class First(object):

    n = 0

    def __init__(self, color='red'):
        self.color = color

    def hello1(self):
        print("Hello from first class!")

    def color_method(self):
        print("My color from first class", self.color)


class Second(First):

    def hello2(self):
        print("Hello from second class!")
        print(self.n, "is my favorite number")


a0 = First()
a0.color_method()
print('-------')
a1 = First(color='blue')
a1.hello1()
a1.color_method()
print('-------')
a2 = Second(color='white')
a2.hello1()
a2.hello2()
a2.color_method()

