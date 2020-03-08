"""
python ping2.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from threading import Thread
import os

num1 = 2
num2 = 1
dat = "ping -c 1 127.0.0.%d" % num1
dat1 = "ping -c 1 127.0.0.%d" % num2

my_list = [dat, dat, dat1]


def my_thread(ping_cmd):
    os.system(ping_cmd)


for i in range(len(my_list)):
    print(i)
    x = Thread(target=my_thread, args=(my_list[i],))
    x.start()
