#!/usr/bin/python
#listbox.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()
l=Listbox(root,width=10)
l.pack(padx=10,pady=5)
list=['John','Jane','Doe']
for i in list:
        l.insert(END, i)
root.mainloop()

