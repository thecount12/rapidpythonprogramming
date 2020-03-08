"""
listbox.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
l_box = Listbox(root, width=10)
l_box.pack(padx=10, pady=5)
a_list = ['John', 'Jane', 'Doe']
for i in a_list:
    l_box.insert(END, i)
root.mainloop()

