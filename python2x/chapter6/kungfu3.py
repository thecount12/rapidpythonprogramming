#!/usr/bin/python
#kungfu1.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming

class KungFu(object):
	mystr="The master"
	def crane(self):
		print "crane kick"
class Master(KungFu):
	mystr="Student is not the master"
	def crane(self,bstr):
		print "must learn crane kick"
teacher=Master() 
teacher.crane(1)
