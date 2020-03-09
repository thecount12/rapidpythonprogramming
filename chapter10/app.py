"""
app.py
Chapter 10 WxWidgets
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from PythonCard import model
from bfile import *


class Minimal(model.Background):

    def on_b_submit_mouse_lick(self, event):
        name_f = str(self.components.fname.text)
        name_l = str(self.components.lname.text)
        self.components.stest.text = ' '
        file_write(name_f)
        file_write(name_l)
        self.components.fname.text = ' '  # clear text field
        self.components.lname.text = ' '  # clear
        self.components.stest.visible = 1
        self.components.stest.text = name_f


if __name__ == '__main__':
    app = model.Application(Minimal)
    app.MainLoop()
