"""
ABC 1
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
    pass

a = B(4)
