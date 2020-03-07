#!/usr/bin/python
#des.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming



class Des():
        def __init__(self, x):
                self.x = x
                print self.x, 'ready'

        def __del__(self):
                print self.x-1, 'destroyed'
		
x = Des(1)

