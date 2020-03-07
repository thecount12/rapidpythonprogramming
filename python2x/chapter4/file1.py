#!/usr/bin/python
# file1.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


blah = open("data.txt", "r")
print blah.readlines()
blah.close()
