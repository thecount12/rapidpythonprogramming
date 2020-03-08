"""
stockspread.py
Chapter 9 Tkinter
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from tkinter import *


def my_insert():
    shares = e1.get()
    entry = e2.get()
    exit_num = e3.get()
    cost = "Cost to get in: $%.2f" % (int(shares) * float(entry))
    exit_result = "Exit: $%.2f" % (int(shares) * float(exit_num))
    profit = ((int(shares) * float(exit_num)) - (int(shares) * float(entry)))
    profit_result = "Profit: $%.2f" % profit
    for item in [cost, exit_result, profit_result]:
        list_b.insert(END, item)


def my_clear():
    list_b.delete(0, END)


root = Tk()

label = Label(root, text="Quantity Shares").grid(row=0)
label2 = Label(root, text="Entry Price").grid(row=1)
label3 = Label(root, text="Exit Price").grid(row=2)


e1 = Entry(root, bg='white')
e2 = Entry(root, bg='white')
e3 = Entry(root, bg='white')

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

button = Button(root, text='calculate', command=my_insert)
button.grid(row=3, column=1)

clear_b = Button(root, text="clear", command=my_clear)
clear_b.grid(row=3, column=0)

list_b = Listbox(root, bg='light blue')
list_b.grid(row=4, column=1, padx=20, pady=20)

root.mainloop()
