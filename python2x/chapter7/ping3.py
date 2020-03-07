#!/usr/bin/python
#ping3.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import os
import thread

num1=2
num2=1 
dat="ping -c 1 127.0.0.%d" % num1 
dat1="ping -c 1 127.0.0.%d" % num2 
def mythread(t,x): 
a=os.system(x) 

print "thread %s" % t
lock.release()
lock=thread.allocate_lock()
z=thread.start_new_thread(mythread, ("thread0",dat1,))
v=thread.start_new_thread(mythread, ("thread1",dat,))
