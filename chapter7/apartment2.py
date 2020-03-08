"""
apartment.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


class Complex(object):

    def __init__(self, unit, parking, pool, rooms, people):
        self.unit = unit
        self.parking = parking
        self.pool = pool
        self.rooms = rooms
        self.people = people


myCo = Complex(10, 8, 1, 20, 15)

# myCo.unit=10
# myCo.parking=8
# myCo.pool=1
# myCo.rooms=20
# myCo.people=15

# comment out the next two blocks
capacity = float(myCo.people)/myCo.rooms
uncovered = 100 - (float(myCo.parking) / myCo.people * 100)
myCo.rooms = 10 * 2
free_rooms = myCo.rooms-myCo.people

print("The complex is at %g capacity" % capacity)
print("There are %g percent people with uncovered parking" % uncovered)
print("We have %g rooms" % myCo.rooms)
print("We have %g free rooms left" % free_rooms)

