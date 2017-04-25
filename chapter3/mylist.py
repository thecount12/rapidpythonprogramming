#!/usr/bin/python
# mylist.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming

mylist = ['cpu', 'monitor', 'printer', 'keyboard', 'mouse']
print 'mylist contains the following:',
for i in mylist:
        print i
print "I have",len(mylist), 'items in mylist'
print "I am adding ink to mylist"
mylist.append('ink')
print "mylist append: ",mylist
mylist.sort()
print "mylist sorted: ",mylist
print "first item in mylist: ",mylist[0]
print "second item in mylist: ",mylist[1]
del mylist[1]
print "removed second item in mylist: ",mylist

