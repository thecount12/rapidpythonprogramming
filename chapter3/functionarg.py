#!/usr/bin/python
# functionarg.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


def table_leaf(a, b=5):
    return a * b


print(table_leaf(5, 10))
print(table_leaf(5))


