"""
case.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


print("0: exit")
print("1: sqr 4")
print("2: list 1-10")
print("3: print even list 1-10")

data = int(input("Enter 0-3: "))


x = 4


def my_exit():
    print("you exited")


def sqr():
    print(x * x)


def a_list():
    for i in range(10):
        print(i)


def even():
    for j in range(1,10):
        if j % 2 == 0:
            print(j)


blah = {0: my_exit, 1: sqr, 2: a_list, 3: even}
blah[data]()


