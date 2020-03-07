"""
mystruct.py
Chapter 4 Files
Author: William C. Gunnells
Rapid Python Programming
"""


import struct
# i represents integer
# c represents character 

bdata = struct.pack("icc", 42, b'A', b'Z')
print(bdata)
# unpack yields a tuple of data 
tdata = struct.unpack("icc", bdata)
print(tdata) 
