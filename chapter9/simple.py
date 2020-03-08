"""
simple.py
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
    b.mainloop()


m_button("Press me")


