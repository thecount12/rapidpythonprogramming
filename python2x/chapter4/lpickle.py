#!/usr/bin/python
#lpickle.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


import pickle
filePickle = open ( 'pickleFile.txt' )
list = pickle.load ( filePickle)
list

for i in list:
 print i

dict = pickle.load (filePickle)
dict

for i in dict:
 print i

dict['firstname']


for i, j in dict.iteritems():
        print i, j

filePickle.close()

