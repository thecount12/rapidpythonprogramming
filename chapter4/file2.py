#!/usr/bin/python
# file2.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


blah = open("data.txt", "r")
a_list = blah.readline()
# a_list = blah.readlines()
for i in a_list:
	print(i)
blah.close()
