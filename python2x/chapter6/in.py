#!/usr/bin/python
#in.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming


class first():
 	n = 0 
	def __init__(self, color='red'):
		self.color = color
	def Hello1(self):
		print "Hello from first class!"
	def Color(self):
		print "My color from first class", self.color

class second(first):
	def Hello2(self):
		print "Hello from second class!"
		print self.n, "is my favorite number"


a0=first()
a0.Color()
print '-------'
a1=first('blue')
a1.Hello1()
a1.Color()
print '-------'
a2=second('white')
a2.Hello1()
a2.Hello2()
a2.Color()

