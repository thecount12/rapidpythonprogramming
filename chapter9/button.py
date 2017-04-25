#!/usr/bin/python
#button.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Tkinter import *

root = Tk()
b= Button(root, text = 'python',command='', width = '2', height='2', activebackground='blue', bg='white', fg='red')
b.pack(padx = 20, pady=20)
root.mainloop()

