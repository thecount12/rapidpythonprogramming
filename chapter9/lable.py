"""
label.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
label = Label(root, font=("helvetica", 15),
              fg='black',
              text='python and tkinter'
              )
label.pack(padx=10, pady=10)
root.mainloop()
