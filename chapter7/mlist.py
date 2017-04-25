#!/usr/bin/python
#mlist.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import itertools

def mlist():
	print "a"
	yield "one"
	print "b"
	yield "two"
	print "c"
	yield "three"
	print "d"
	yield "four"
	print "e"
	yield "five"
	print "f"
	yield "six"
	print "g"
	yield "seven"
	print "h" 
for i in mlist():
	print i
for x,y in zip([0], mlist()):
	print x, y 
for x,y in zip([0,1,2], mlist()): 
	print x, y
for x,y in zip([j for j in range(9) if j>5], mlist()):
	print x,y
for x,y in zip([j for j in range(9)], mlist()): 
	print x,y 
for x,y in zip([j for j in range(9)], mlist()):
	print x
for x,y in zip([j for j in range(9)], mlist()):
	print y 

list(itertools.islice(mlist(),4))
list(itertools.islice(mlist(),10)) 
