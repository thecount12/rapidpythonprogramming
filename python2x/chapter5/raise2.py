#!/usr/bin/python
#raise2.py
# Chapter 5 Exceptions 
# Author: William C. Gunnells
# Rapid Python Programming

import sys
def letserror():
	raise RuntimeError('Force the error')
def main():
	try:
		letserror()
	except Exception, err:
		sys.stderr.write(str(err))
main()
