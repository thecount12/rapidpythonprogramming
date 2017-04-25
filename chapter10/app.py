#!/usr/bin/python
#app.py
# Chapter 10 WxWidgets 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from PythonCard import model
from bfile import *

class Minimal(model.Background):
	def on_bsubmit_mouseClick(self, event):
		namef = str(self.components.fname.text)
		namel = str(self.components.lname.text)
		self.components.stest.text=' '
		FileWrite(namef) 
		FileWrite(namel)
		self.components.fname.text=' ' # clear text field
		self.components.lname.text=' ' # clear
		self.components.stest.visible=1
		self.components.stest.text=namef

if __name__ == '__main__':
	app = model.Application(Minimal)
	app.MainLoop()
