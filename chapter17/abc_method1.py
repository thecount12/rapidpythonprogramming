"""
ABC 2
"""

from abc import ABC, abstractmethod


class MyAbstract(ABC):
    def __init__(self, my_value):
        self.value = my_value
        super().__init__()

    @abstractmethod
    def do_something(self):
        print(self.value)


class B(MyAbstract):
    def do_something(self):
        return self.value + 38


class Foo(MyAbstract):
    def do_something(self):
        return self.value * 25


a = B(4)
b = Foo(4)
print(a.do_something())
print(b.do_something())
