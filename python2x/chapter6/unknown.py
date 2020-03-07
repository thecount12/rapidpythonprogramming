#!/usr/bin/python
#unknown.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming


class bar: 
	def blah(self): 
		print "cool" 
	def strange(self): 
		print "wow" 
	def nice(self): 
		print "very cool now"
	def bazinga(self):
		print "bazinga" 
class foo(bar): 
	def __iter__(self): # iterate unknown
		return iter(vars(bar)) # vars built-in attr
a=foo()
for i in a: 
	print i 
