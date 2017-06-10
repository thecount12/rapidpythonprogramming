#!/usr/bin/python
# stockspread.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming

# notes:
# script to caclucate potential profit
# requires quantity of shares purchased at entry and exit
# print quantity

# libs
from Tkinter import *

# prototype
#shares=raw_input("Enter quantity of shares: ")
#entry=raw_input("Enter price per share: ")
#exit=raw_input("Enter future exit price per share: ")
#print "Cost to get in: $%f" % ( int(shares) * float(entry))
#print "Exit: $%f" % ( int(shares) * float(exit) )
#profit = ( (int(shares) * float(exit) ) -   (int(shares) * float(entry)) )
#print "Profit: $%f" % profit 


def myinsert(): 

	shares=e1.get()
	entry=e2.get()
	exit=e3.get()
	cost="Cost to get in: $%.2f" % ( int(shares) * float(entry))
	exitresult="Exit: $%.2f" % ( int(shares) * float(exit))
	profit=( (int(shares) * float(exit) ) - (int(shares) * float(entry)) )
	profitresult="Profit: $%.2f" % profit
	for item in [cost,exitresult,profitresult]:
		listb.insert(END,item)

def myclear():
	listb.delete(0,END)

root=Tk()

label=Label(root, text="Quantity Shares").grid(row=0)
label2=Label(root,text="Entry Price").grid(row=1)
label3=Label(root,text="Exit Price").grid(row=2)


e1=Entry(root,bg='white')
e2=Entry(root,bg='white')
e3=Entry(root,bg='white')

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

button=Button(root, text='calculate', command=myinsert)
button.grid(row=3,column=1)

clearb=Button(root, text="clear",command=myclear)
clearb.grid(row=3,column=0)

listb=Listbox(root,bg='light blue')
listb.grid(row=4,column=1, padx=20,pady=20)

root.mainloop()
