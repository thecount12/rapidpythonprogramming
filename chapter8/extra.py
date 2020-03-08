"""
use and import apartment4.py
extra.py
"""


# lib
from apartment4 import *
from easygui import *

msg = "Enter Fields"
title = "Apartment Complex"
fieldNames = ["unit", "parking",
              "pool", "rooms", "people"]
fieldValues = []

fieldValues = multenterbox(msg, title,
                           fieldNames,
                           fieldValues
                           )
fd = fieldValues  # print fd[0]
myCo = Complex(int(fd[0]), int(fd[1]), int(fd[2]),
               int(fd[3]), int(fd[4]))

data = []
for i in myCo.result(): 
    data.append(i+"\n")

textbox("apt data", "Apartment Complex", data) 

