#!/usr/bin/python 
#simpled.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

def mlabel():
	l=Label(root, text='My Python repeating', fg='red')
	l.pack()

def mbutton(mess,m):
	b=Button(root,text=mess,command=m)
	b.pack()

def tbox():
	t=Text(root)
	t.pack()

def lbox(list):
	lb=Listbox(root)
	lb.pack()
	for i in list:
		lb.insert(END, i)

root=Tk()
mbutton("Press me",mlabel)
#mlabel("My Python")
tbox()
lbox(['milk', 'cheese', 'fruit', 'chicken'])
root.mainloop()
