#!/usr/bin/python
#third.py
# Chapter 10 WxWidgets 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import wx

class Blah(wx.Frame):
	def __init__(self,x,y,z):
		wx.Frame.__init__(self,x,y,z)

app=wx.PySimpleApp()
frame=Blah(x=None, y=-1,z="wow") 
frame.Show()
app.MainLoop()


