#!/usr/bin/python
# file.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


blah = open("data.txt", "r")
blah.seek(5)
print(blah.readline())
blah.close()

