"""
parse.py
Chapter 4 Files
Author: William C. Gunnells
Rapid Python Programming
"""


blah = open("data.txt", "r") 
a_list = blah.readlines()
search1 = ""
search2 = ""
for line in a_list:
    if 'love' in line:
        search1 = line
print(f"found line with: {search1} in file")
change = search1.split()
print(change)
print(change[1])
for item in change:
    if 'python' in item:
        search2 = item
print(f"found {search2} on line that also contained {change[1]}")
blah.close() 
