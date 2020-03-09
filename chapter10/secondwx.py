"""
second.py
Chapter 10 WxWidgets
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import wx


class Blah(wx.App):

    def OnInit(self):
        frame = wx.Frame(None, -1, "I love python")
        frame.Show(True)
        self.SetTopWindow(frame)
        return 1


app = Blah()
app.MainLoop()

