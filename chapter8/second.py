"""
second.py with image pythonlogo.jpg
Chapter 8 EasyGUI
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from easygui import *

image = "logo.gif"
msgbox("My new Logo", "EasyGui Tool",
       ok_button="Enter", image=image)

