#!/usr/bin/python
#classinit.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming


class hello:
        def __init__(self,name):
                self.name=name
        def blah(self):
                print "Hello world, my name is",self.name

a=hello('William')
a.blah()


