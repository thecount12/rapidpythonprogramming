"""
mylist.py
Chapter 3 input
Author: William C. Gunnells
Rapid Python Programming
"""


my_list = ['cpu', 'monitor',
           'printer', 'keyboard',
           'mouse']
print('my_list contains:')
for i in my_list:
    print(i)
print("I have", len(my_list), 'items in my_list')
print("I am adding ink")
my_list.append('ink')
print("my_list append: ", my_list)
my_list.sort()
print("my_list sorted: ", my_list)
print("first item: ", my_list[0])
print("second item: ", my_list[1])
del my_list[1]
print("removed second item: ", my_list)

