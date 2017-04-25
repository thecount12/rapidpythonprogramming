#!/usr/bin/python
#ent.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root=Tk()
root.geometry('200x210+350+70')
ent=Entry(root, bg='white')
ent.pack()
button=Button(root, text='press me', command='')
button.pack()
listb=Listbox(root,bg='blue')
listb.pack()
root.mainloop()
