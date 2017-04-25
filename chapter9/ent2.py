#!/usr/bin/python
#ent2.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

def myinsert(): #3
        name = ent.get() 
        print name 
        listb.insert(END,name) 
        ent.delete(0,END)  

root=Tk()
root.geometry('200x210+350+70')
ent=Entry(root, bg='white')
ent.pack(anchor=W)
button=Button(root, text='press me', command=myinsert)
button.pack(pady=20, anchor=E)
listb=Listbox(root,bg='blue')
listb.pack()
root.mainloop()
