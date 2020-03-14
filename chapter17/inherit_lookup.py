"""
lookup example
"""


class Animal(object):
    def __init__(self, animal):
        self.animal = animal

    def get_animal(self):
        return 'I am a {}'.format(self.animal)


class Eat(Animal):
    def get_food(self):
        return 'I eat {} food'.format(self.animal)


foo = Animal('cat')
print(foo.get_animal())
bar = Eat('dog')
print(bar.get_animal())
print(bar.get_food())
