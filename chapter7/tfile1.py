"""
tfile1.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


with open("blah.txt", "r") as f:
    my_list = f.readlines()


def mygen(data):
    for lines in data:
        yield lines


if __name__ == "__main__":
    for i in mygen(my_list):
        print(i)
