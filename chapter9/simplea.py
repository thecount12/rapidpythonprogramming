#!/usr/bin/python 
#simplea.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()

def mbutton(mess):
	b=Button(root,text=mess)
	b.pack()

def mlabel(lab):
	l=Label(root, text=lab)
	l.pack()
	
mbutton("Press me")
mlabel("My Python")
root.mainloop()
