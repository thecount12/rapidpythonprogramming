#!/usr/bin/python
#python ping2.py 
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from Threads!threadingthreading import Thread
import os

num1=2
num2=1 
dat="ping -c 1 127.0.0.%d" % num1 
dat1="ping -c 1 127.0.0.%d" % num2 

def mythread(x): 
	a=os.system(x) 

a=Thread(target=mythread, args=(dat1,))
c=Thread(target=mythread, args=(dat,))
b=Thread(target=mythread, args=(dat,))
a.start()
b.start()
c.start()
