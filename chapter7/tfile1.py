#!/usr/bin/python
#tfile1.py 
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

f=open("blah.txt","r")
def mygen(f):
	for i in f.readlines(): 
		yield i 
if __name__=="__main__":
	a=mygen(f)
	for i in a:
		print i
	f.close()
