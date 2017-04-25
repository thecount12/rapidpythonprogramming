#!/usr/bin/python 
#simplec.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

def mbutton(mess):
	b=Button(root,text=mess)
	b.pack()

def mlabel(lab):
	l=Label(root, text=lab)
	l.pack()

def tbox():
	t=Text(root)
	t.pack()

def lbox(list):
	lb=Listbox(root)
	lb.pack()
	for i in list:
		lb.insert(END, i)

root=Tk()
mbutton("Press me")
mlabel("My Python")
tbox()
lbox(['milk', 'cheese', 'fruit', 'chicken'])
root.mainloop()
