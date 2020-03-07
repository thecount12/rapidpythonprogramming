#!/usr/bin/python
#case.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming


print "0: exit"
print "1: sqr 4"
print "2: list 1-10"
print "3: print even list 1-10"

data=int(raw_input("Enter 0-3: "))


x=4
def exit():
	print "you exited"
def sqr():
	print x*x 
def list(): 
	for x in range(10):
		print x
def even():
	for x in range(1,10):
		if x % 2 == 0:
			print x

blah={0: exit, 1: sqr, 2: list, 3: even }
blah[data]()


