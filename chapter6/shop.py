"""
shop.py
Chapter 6 Object Oriented programming
Author: William C. Gunnells
Rapid Python Programming
"""


class Cart(object):

    def __init__(self):
        self.food = "beans"
        self.amt = 0

    def buy_food(self, amt):
        self.amt += amt
        print("You purchased", amt, "cans", self.food)


checkout = Cart()
checkout.buy_food(5)

