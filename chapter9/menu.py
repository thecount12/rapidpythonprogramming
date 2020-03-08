"""
menu.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
m = Menu(root)
file_menu = Menu(m, tearoff=0)
file_menu.add_command(label='Exit')
m.add_cascade(label='File', menu=file_menu)
root.config(menu=m)
root.mainloop()

