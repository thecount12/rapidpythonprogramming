"""
button.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
b = Button(root, text='python', command='', width='10',
           height='10', activebackground='blue',
           bg='white', fg='red'
           )
b.pack(padx=20, pady=20)
root.mainloop()

