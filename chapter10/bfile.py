"""
basic file write
bfile.py
Chapter 10 WxWidgets
Author: William C. Gunnells
Rapid Python Programming
"""


def file_write(data):
    with open('file.txt', 'a') as f:
        f.write(data)


if __name__ == '__main__':
    d = input("enter something: ")
    file_write(d)
