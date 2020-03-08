"""
scroll
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *

root = Tk()
f = Frame(root, bg='blue')
m_scroll = Scrollbar(f, bg='green')
text = Text(f, width=20, height=10,
            yscrollcommand=m_scroll.set)
m_scroll.config(command=text.yview)
m_scroll.pack(side=RIGHT, fill=Y)
text.pack()
f.pack()
root.mainloop()

