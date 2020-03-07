"""
conditions.py
Chapter 2 basic flow control, conditions and indention
Author: William C. Gunnells
"""


x = 3
if x < 4:
    print(f"x is < 4, x is {x}")

if x < 4 or x > 2:
    print(f"x is < 4 and > 2, x={x}")
if x == 1:
    print("Item 1")
elif x == 2:
    print("Item 2 - true value")
elif x == 3:
    print("Item 3 - true value")
else:
    print("Default option if None listed")

for i in [1, 2, 3, 4, 5]:
    print(f"Iteration #{i}")

for i in range(5):
    print(i)

while x < 10:
    print(f"while iteration: {x}")
    x = x + 1


