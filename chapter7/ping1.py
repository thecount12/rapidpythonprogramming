"""
ping1.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import os

num1 = 2
num2 = 1
dat = "ping -c 1 127.0.0.%d" % num1
dat1 = "ping -c 1 127.0.0.%d" % num2

# a = os.system(dat1)
# a = os.system(dat)


def my_thread(x):
    os.system(x)


my_thread(dat1)
my_thread(dat)
