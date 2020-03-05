#!/usr/bin/python
#shop.py
# Chapter 6 Object Oriented programming 
# Author: William C. Gunnells
# Rapid Python Programming


class cart():
        def __init__(self):
                self.food = "beans"
                self.amt = 0
        def buyfood(self,amt):
                self.amt += amt
                print "You purchased" ,amt,"cans",self.food

checkout = cart()
checkout.buyfood(5)

