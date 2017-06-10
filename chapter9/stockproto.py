#!/usr/bin/python
#stockproto.py
# Chapter 9 Tkinter 
# Author: William C. Gunnells
# Rapid Python Programming


shares=raw_input("Enter quantity of shares: ")
entry=raw_input("Enter price per share: ")
exit=raw_input("Enter future exit price per share: ")
print "Cost to get in: $%f" % ( int(shares) * float(entry))
print "Exit: $%f" % ( int(shares) * float(exit))
profit = ( ( int(shares) * float(exit) ) - (int(shares) * float(entry)) )
print "Profit: $%f" % profit
