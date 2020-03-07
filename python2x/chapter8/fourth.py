#!/usr/bin/python
#fourth.py 
# Chapter 8 EasyGUI 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from easygui import *

filename=("data.csv")
file=open(filename, "r")
text = file.readlines()
file.close()
codebox("Contents" + filename, "Display File", text)


