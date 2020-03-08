"""
frame.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
frame = Frame(root, bg='green',
              width=200, height=200)
frame.pack(padx=10, pady=10)
root.mainloop()

