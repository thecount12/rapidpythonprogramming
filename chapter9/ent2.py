"""
ent2.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *


def my_insert():
    name = ent.get()
    print(name)
    list_b.insert(END, name)
    ent.delete(0, END)


root = Tk()
root.geometry('200x210+350+70')
ent = Entry(root, bg='white')
ent.pack(anchor=W)
button = Button(root, text='press me', command=my_insert)
button.pack(pady=20, anchor=E)
list_b = Listbox(root, bg='blue')
list_b.pack()
root.mainloop()
