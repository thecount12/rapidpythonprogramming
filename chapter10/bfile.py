#!/usr/bin/python
# basic file write
#bfile.py
# Chapter 10 WxWidgets 
# Author: William C. Gunnells
# Rapid Python Programming


def FileWrite(d):
	f=open('file.txt','a')
	f.write(d)
	f.close()

if __name__=='__main__':
	d=raw_input("enter something: ")
	FileWrite(d)
