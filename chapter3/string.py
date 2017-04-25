#!/usr/bin/python
#string.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


mystring = "Learning Practical Python"
if 'earning' in mystring:
	print 'found earning'
else:
	print 'did not find string pattern'

if mystring.startswith('Learn'):
	print 'found Learn startswith' 

if mystring.find('earn') != -1:
	print 'found earn with find'

change = mystring.split()
print change
delimit = ';'
new = delimit.join(change)
print new
comm = new.split(';')
print comm
	

	
