"""
third.py
Chapter 8 EasyGUI
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from easygui import *

result = []
blah = open("data.csv", "r")
for i in blah.readlines():
    result.append(i)

textbox("data", "title", result)
# don't forget you can still use console
print(result)
blah.close()

