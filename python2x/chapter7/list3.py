#!/usr/bin/python
#list3.py
# Chapter 7 Cool Features of Python
# Author: William C. Gunnells
# Rapid Python Programming

square=[i**2 for i in range(10)]
factor=[2**i for i in range(10)]
evenSquare=[x for x in square if x % 2 == 0]
oddSquare=[x for x in square if x % 2 == 1]
print square; print factor; print evenSquare; print oddSquare


