#!/usr/bin/python
#menu.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()
m=Menu(root)
filemenu=Menu(m,tearoff=0)
filemenu.add_command(label='Exit')
m.add_cascade(label='File', menu=filemenu)
root.config(menu=m)
root.mainloop()

