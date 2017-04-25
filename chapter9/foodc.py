#!/usr/bin/python
#foodc.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()
listb=Listbox(root)
listb.pack()
list= ['milk', 'cheese', 'fruit', 'chicken'] 
for item in list:
	listb.insert(END, item)
print list 
root.mainloop()
