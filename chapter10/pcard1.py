"""
pcard1.py
Chapter 10 WxWidgets
Author: William C. Gunnells
Rapid Python Programming
"""


from PythonCard import model


class Blah(model.Background):
    pass


if __name__ == "__main__":
    app = model.Application(Blah)
    app.MainLoop()


