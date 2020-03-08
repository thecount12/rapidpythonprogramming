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
        self.capacity = 0
        self.uncovered = 0
        self.free_rooms = 0

    def calc(self):
        self.capacity = float(self.people) / self.rooms
        self.uncovered = 100 - (float(self.parking) / self.people * 100)
        self.rooms = 10 * 2
        self.free_rooms = self.rooms - self.people

    def result(self):
        self.calc()
        a = "The complex is at %g capacity" % self.capacity
        b = "There are %g percent people with uncovered parking" % self.uncovered
        c = "We have %g rooms" % self.rooms
        d = "We have %g free rooms left" % self.free_rooms
        data = [a, b, c, d]
        return data


if __name__ == "__main__":
    myCo = Complex(10, 8, 1, 20, 15)
    myCo.result()
    for i in myCo.result():
        print(i)
