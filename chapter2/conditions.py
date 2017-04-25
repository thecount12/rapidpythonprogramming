#!/usr/bin/python
# conditions.py
# Chapter 2 basic flow control, conditions and indention
# Author: William C. Gunnells

x=3
if x < 4:
 print "x is less then 4 x is ",x  # notice the space (is ",x)

if (x < 4 or x > 2):
 print "x is less then 4 and greater then 2, x=", x # notice (x=", x)

if x == 1:
   print "Item 1 - true value", x
elif x == 2:
   print "Item 2 - true value", x
elif x == 3:
   print "Item 3 - true value", x
else:
   print "Default option if none listed", x

for i in [1,2,3,4,5]:
 print "Iteration #", i

for i in range(5):
 print i

while (x< 10):
 print "while interation is.", x
 x=x+1


