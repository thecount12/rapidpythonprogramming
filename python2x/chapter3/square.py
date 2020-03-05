#!/usr/bin/python
# square.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming

import sys

def square(x):
	return x*x
if len(sys.argv) !=2:
	print 'Need an integer'
	sys.exit(1)

x = int(sys.argv[1])
print 'square is %g' % square(x)

