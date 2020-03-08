"""
canvas.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
c = Canvas(root, width='80',
           height='60',
           bg='white'
           )
c.pack(padx=5, pady=5)
s = c.create_line(10, 30, 10, 30,
                  40, 10, 20, 45,
                  30, 80)
root.mainloop()

