#!/usr/bin/python
# mytuple.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming

mytuple = ('pen', 'pencils', 'paper')
print 'mytuple contains: ',mytuple
print 'I have',len(mytuple), 'in mytuple'
drawer = ('ruler', 'paperclips', mytuple)
print 'mytuple and drawer contain: ',drawer
print 'first item in first tuple is : ',drawer[2][0]

