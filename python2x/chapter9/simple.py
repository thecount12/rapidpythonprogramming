#!/usr/bin/python 
# simple.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()

def mbutton(mess):
	b=Button(root,text=mess)
	b.pack()
	b.mainloop()

mbutton("Press me")


