"""
fourth.py
Chapter 10 WxWidgets
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import wx


class Blah(wx.Frame):

    def __init__(self, x, y, z):
        wx.Frame.__init__(self, x, y, z)
        panel = wx.Panel(self)
        button = wx.Button(panel, label="press me")


app = wx.PySimpleApp()
frame = Blah(x=None, y=-1, z="wow")
frame.Show()
app.MainLoop()


