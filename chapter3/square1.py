#!/usr/bin/python
# square1.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


import sys


def square(sq):
	return sq * sq


if len(sys.argv) != 2:
	print('Need an integer')
	sys.exit(1)

x = int(sys.argv[1])
print('square is %g' % square(x))
