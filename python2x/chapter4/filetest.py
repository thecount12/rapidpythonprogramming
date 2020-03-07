#!/usr/bin/python
#filetest.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


f = open("dat.txt", "wb") 
print "Name the file: ", f.name 
print "Closed or open: ", f.closed 
print "mode: ", f.mode 
print "Softspace: ", f.softspace
