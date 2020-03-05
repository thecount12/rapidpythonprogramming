#!/usr/bin/python
# mytuple.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming

my_tuple = ('pen', 'pencils', 'paper')
print('my_tuple contains: ', my_tuple)
print('I have', len(my_tuple), 'in mytuple')
drawer = ('ruler', 'paperclips', my_tuple)
print('my_tuple and drawer contain: ', drawer)
print('first item in first tuple is : ', drawer[2][0])

