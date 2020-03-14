"""
abc animal
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, animal):
        self.animal = animal
        super().__init__()

    @abstractmethod
    def get_animal(self):
        print('I am a {}'.format(self.animal))

    @abstractmethod
    def talk(self):
        print("I make incredible noise")


class Eat(Animal):
    def get_food(self):
        return 'I eat {} food'.format(self.animal)

    def get_animal(self):
        return 'I am the greatest {}'.format(self.animal)

    def talk(self):
        return "I talk like a {}".format(self.animal)

    def get_original_animal(self):
        super().get_animal()

    def get_original_talk(self):
        super().talk()


# foo = Animal('cat’).  # violates ABC
# print(foo.get_animal())  # violates ABC
bar = Eat('dog')
print(bar.get_animal())
print(bar.get_food())
print(bar.talk())
bar.get_original_animal()
bar.get_original_talk()
