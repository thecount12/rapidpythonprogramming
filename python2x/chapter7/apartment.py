#!/usr/bin/python
#apartment.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming


'''
required information:10 units with 2 bedrooms, 
8 covered parking
1 pool, x rooms, 15 people
'''

unit=10
parking=8
pool=1
rooms=20
people=15

capacity=float(people)/rooms
uncovered=100-(float(parking)/people*100)
rooms=10*2
freerooms=rooms-people

print "The complex is at %g capacity" % capacity
print "There are %g percent people with uncovered parking" % uncovered
print "We have %g rooms" % rooms
print "We have %g free rooms left" % freerooms

