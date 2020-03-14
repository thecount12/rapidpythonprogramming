"""
Polymorphism Test
"""


class Animal(object):
    count = 0

    def __init__(self, name):
        self.animal = name
        Animal.count += 1

    def play(self):
        return '{} loves to play'.format(self.animal)

    def get_count(self):
        return Animal.count


class Cat(Animal):
    def animal_type(self):
        return "{} is a cat".format(self.animal)

    def eat_food(self):
        return "{} eats cat food".format(self.animal)


class Dog(Animal):
    def animal_type(self):
        return "{} is a dog".format(self.animal)

    def eat_food(self):
        return "{} eats dog food".format(self.animal)


for animal in (Cat("fluffy"), Dog("Rover")):
    print(animal.animal_type())
    print(animal.play())
    print(animal.eat_food())
    print("instance: {}".format(animal.get_count()))
