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

class complex:
	def __init__(self, unit, parking, pool, rooms, people):	
		self.unit=unit
		self.parking=parking
		self.pool=pool
		self.rooms=rooms
		self.people=people
	def calc(self):
		self.capacity=float(self.people)/self.rooms
		self.uncovered=100-(float(self.parking)/self.people*100)
		self.rooms=10*2
		self.freerooms=self.rooms-self.people
	def result(self):
		print "The complex is at %g capacity" % self.capacity
		print "There are %g percent people with uncovered parking" % self.uncovered
		print "We have %g rooms" % self.rooms
		print "We have %g free rooms left" % self.freerooms


myCo=complex(10,8,1,20,15)
myCo.calc()  # these are tied together initialize
myCo.result() # these are tied together

#myCo.unit=10
#myCo.parking=8
#myCo.pool=1
#myCo.rooms=20
#myCo.people=15

#comment out the next two blocks
#capacity=float(myCo.people)/myCo.rooms
#uncovered=100-(float(myCo.parking)/myCo.people*100)
#myCo.rooms=10*2
#freerooms=myCo.rooms-myCo.people

#print "The complex is at %g capacity" % capacity
#print "There are %g percent people with uncovered parking" % uncovered
#print "We have %g rooms" % myCo.rooms
#print "We have %g free rooms left" % freerooms

