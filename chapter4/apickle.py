#!/usr/bin/python
# apickle.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


import pickle
filePickle = open('pickleFile.txt', 'wb')
list1 = ['I', 'love', 'python', 1, 2, 3, 'ok']
list2 = {'firstname': 'john', 'lastname': 'doe', 1: 'one'}
pickle.dump(list1, filePickle)
pickle.dump(list2, filePickle)
filePickle.close()


