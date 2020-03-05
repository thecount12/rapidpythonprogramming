#!/usr/bin/python
# string.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


my_string = "Learning Practical Python"
if 'earning' in my_string:
    print('found earning')
else:
    print('did not find string pattern')
if my_string.startswith('Learn'):
    print('found Learn startswith')
if my_string.find('earn') != -1:
    print('found earn with find')
change = my_string.split()
print(change)
delimit = ';'
new = delimit.join(change)
print(new)
comm = new.split(';')
print(comm)

