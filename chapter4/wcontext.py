"""
wcontext.py
Chapter 4 Files
Author: William C. Gunnells
Rapid Python
"""


with open('output.txt', 'w') as f:
    f.write("Usual Hello World\nNext line is cool")

with open("output.txt", 'r') as r:
    data = r.readlines()

for i in data:
    print(i)
