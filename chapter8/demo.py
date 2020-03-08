"""
demo.py
Chapter 8 EasyGUI
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from easygui import *
import sys

while 1:
    msgbox("Hello, world!")

    msg = "What is your favorite flavor?"
    title = "Ice Cream Survey"
    choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):
        pass
    else:
        sys.exit(0)


