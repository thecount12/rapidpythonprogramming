#!/usr/bin/python
#scroll
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()
f= Frame(root, bg='blue')
mscroll=Scrollbar(f, bg='green')
text = Text(f, width=20, height=10, yscrollcommand=mscroll.set)
mscroll.config(command=text.yview)
mscroll.pack(side = RIGHT, fill=Y)
text.pack()
f.pack()
root.mainloop()

