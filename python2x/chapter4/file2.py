#!/usr/bin/python
# file2.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


blah = open("data.txt", "r")
list = blah.readline()
#list = blah.readlines()
for i in list:
	print i
blah.close()
