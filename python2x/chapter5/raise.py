#!/usr/bin/python
#raise.py
# Chapter 5 Exceptions 
# Author: William C. Gunnells
# Rapid Python Programming

import sys
def letserror():
	raise RuntimeError('Force the error')
def main():
	letserror()
main()
