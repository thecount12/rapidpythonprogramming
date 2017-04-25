#!/usr/bin/python
#kungfu1.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming

class KungFu(object):
	mystr="The master"
class Master(KungFu):
	mystr="Student is not the master"
teacher=Master.mystr
print teacher

