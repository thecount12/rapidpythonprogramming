"""
basic ABC
"""


class MyAbstract:
    def do_something(self):
        print("MyAbstract")


class B(MyAbstract):
    pass


a = MyAbstract()
a.do_something()
b = B()
b.do_something()
