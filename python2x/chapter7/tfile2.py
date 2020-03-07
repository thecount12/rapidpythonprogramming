#!/usr/bin/python
#tfile2.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from tfile1 import *

mygen(f)

for x,y in zip([z for z in range(9)], mygen(f)):
	print repr(x),repr(y) 
for x,y in zip([z for z in range(9) if z > 5], mygen(f)):
	print x
print "__________________"
for x,y in zip([z for z in range(9) if z > 5], mygen(f)):
	print y 
print "__________________"
for i in mygen(f):
	print i
print list(mygen(f))
f.close()
