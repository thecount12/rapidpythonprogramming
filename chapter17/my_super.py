"""
Super example
"""


class Animal(object):
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)


example = Dog("Rover")
print(example.name)
