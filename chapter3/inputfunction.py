#!/usr/bin/python
# inputfunction.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


def square(sq):
    return sq * sq


x = int(input("Enter a number "))
print("input without function ", x)
print("input with function ", square(2))
