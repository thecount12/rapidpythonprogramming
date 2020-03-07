#!/usr/bin/python
#name.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming

class hello:
        def __init__(self,l,f):
                self.last=l
                self.first=f
        def blah(self):
                print "My first name is", self.first
                print "My last name is", self.last

a=hello('Doe', 'John')
a.blah()


