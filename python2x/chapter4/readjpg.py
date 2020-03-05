#!/usr/bin/python
#readjpg.py
# Chapter 4 Files 
# Author: William C. Gunnells
# Rapid Python Programming


import sys 
import binascii 
import struct

signature=[ 
	binascii.unhexlify(b'FFD8FFD8'), 
	binascii.unhexlify(b'FFD8FFE0'), 
	binascii.unhexlify(b'FFD8FFE1') ]
with open(sys.argv[1],'rb') as file:
	first_four_bytes=file.read(4)
	if first_four_bytes in signature: 
		print("JPEG found.") 
	else: print("This is not a JPEG file.") 
	print first_four_bytes 

	print binascii.hexlify(first_four_bytes) 
	second=file.read(1) 
	while (ord(second) !=0xDA): 
		while (ord(second) !=0xFF): second=file.read(1) 
		while (ord(second) ==0xFF): second=file.read(1) 
		if (ord(second) >=0xC0 and ord(second) <=0xC3): 
			print binascii.hexlify(file.read(3)) 
			print struct.unpack('>HH',file.read(4)) 
