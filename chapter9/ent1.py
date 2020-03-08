"""
ent1.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
root.geometry('200x210+350+70')
ent = Entry(root, bg='white')
ent.pack(anchor=W)
button = Button(root, text='press me', command='')
button.pack(pady=20, anchor=E)
list_b = Listbox(root, bg='blue')
list_b.pack()
root.mainloop()
