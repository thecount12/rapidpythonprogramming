#!/usr/bin/python
#try3.py
# Chapter 5 Exceptions 
# Author: William C. Gunnells
# Rapid Python Programming


try:
	x=int(raw_input("Enter a number: "))
	print x
except EOFError: print "why did you exit early"
except ValueError:
	print "You did not enter a number"
