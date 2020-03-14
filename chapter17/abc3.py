"""
abc 3
"""

from abc import ABC, abstractmethod


class MyAbstract(ABC):

    @abstractmethod
    def do_something(self):
        print("hello")


class InheritBoth(MyAbstract):
    def do_something(self):
        super().do_something()
        print("world")


a = InheritBoth()
a. do_something()
