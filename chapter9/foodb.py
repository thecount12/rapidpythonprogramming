"""
foodb.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""

# lib
from tkinter import *

root = Tk()
list_b = Listbox(root)
list_b.pack()
a_list = ['milk', 'cheese', 'fruit', 'chicken']
print(a_list)
root.mainloop()
