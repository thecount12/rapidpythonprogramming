#!/usr/bin/python
# inventory.py
# Chapter 3 input
# Author: William C. Gunnells
# Rapid Python Programming


inventory = {'monitors': 'two',
             'printers': 5,
             'keyboards': 3}
print(inventory["printers"])
inventory['printers'] = 6
print(inventory['printers'])
print(inventory)
del inventory['keyboards']
print(inventory)
for i, j in inventory.items():
    print(i, j)
