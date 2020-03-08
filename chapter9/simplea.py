"""
simplea.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()


def m_button(mess):
    b = Button(root, text=mess)
    b.pack()


def m_label(lab):
    my_label = Label(root, text=lab)
    my_label.pack()


m_button("Press me")
m_label("My Python")
root.mainloop()
