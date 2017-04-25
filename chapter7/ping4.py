#!/usr/bin/python
#ping4.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import threading

def mythread(x):
	print 'Worker: %s' % x
	return

threads=[]
for i in range(3):
	t=threading.Thread(target=mythread,args=(i,))
	threads.append(t)
	t.start()
