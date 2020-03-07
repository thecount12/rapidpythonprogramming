#!/usr/bin/python
# lpickle.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


import pickle
filePickle = open('pickleFile.txt', "rb")
list1 = pickle.load(filePickle)
for i in list1:
    print(i)

my_dict = pickle.load(filePickle)
for i in my_dict:
    print(i)

for i, j in my_dict.items():
    print(f"{i}: {j}")
filePickle.close()

