#!/usr/bin/python 
# parse.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


blah = open("data.txt", "r") 
list=blah.readlines() 
for i in list: 
	if 'love' in i: 
		new=i
print "print specific line 'love' in file" 
print new
change=new.split() 
print "print specific list in file as a list" 
print change 
print "print specific field in list 'love'" 
print change[1]
for i in change: 
	if 'python' in i: 
		wow=i

print "search for specific field in list 'python' to print wow"
blah.close() 
