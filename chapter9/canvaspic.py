"""
canvaspic.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming

"""

# lib
from tkinter import *

root = Tk()
c = Canvas(root, width='275',
           height='100',
           bg='white')
c.pack(padx=5, pady=5)
photo = PhotoImage(file='jandb.gif')
item = c.create_image(0, 0, anchor=N+W,
                      image=photo)
root.mainloop()
