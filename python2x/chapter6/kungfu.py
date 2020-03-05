#!/usr/bin/python
#kungfu.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming

class KungFu(object):
	mystr="The master"
	pass
class Master(KungFu):
	pass
teacher=Master.mystr
print teacher

