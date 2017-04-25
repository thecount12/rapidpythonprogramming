#!/usr/bin/python
#ping.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming


import os
num1=2 # can't ping 
num2=1 # can ping
dat="ping -c 1 127.0.0.%d" % num1 
dat1="ping -c 1 127.0.0.%d" % num2 
a=os.system(dat1) 
a=os.system(dat) 
