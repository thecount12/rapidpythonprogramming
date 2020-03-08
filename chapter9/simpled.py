"""
simpled.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *


def m_label():
    my_label = Label(root, text='My Python repeating', fg='red')
    my_label.pack()


def m_button(mess, m):
    b = Button(root, text=mess, command=m)
    b.pack()


def t_box():
    my_text = Text(root)
    my_text.pack()


def l_box(a_list):
    my_list_box = Listbox(root)
    my_list_box.pack()
    for i in a_list:
        my_list_box.insert(END, i)


root = Tk()
m_button("Press me", m_label)
# m_label("My Python")
t_box()
l_box(['milk', 'cheese', 'fruit', 'chicken'])
root.mainloop()
