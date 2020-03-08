"""
lambda.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


foo = [1, 2, 3, 4, 5, 6]
print((lambda x: x % 2 == 0, foo))
print(lambda x: x % 2 == 0, [x for x in range(1, 7)])
blah = [x for x in range(1, 7) if x % 2 == 0]
print(blah)


def bar():
    return list(map(lambda x: x % 2 == 0, foo))


print(bar())
