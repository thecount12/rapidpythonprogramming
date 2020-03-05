#!/usr/bin/python
#functionarg-input.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming

def tableLeaf(a,b=5):
        print "area of table:", a*b

x = int(raw_input("enter a number: "))
tableLeaf(x)

