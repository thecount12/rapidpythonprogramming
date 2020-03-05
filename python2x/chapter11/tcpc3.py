#!/usr/bin/python
#tcpc3.py
# Chapter 11 Sockets and Dabases 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import socket

HOST = 'localhost'    
PORT = 8001              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
	data=raw_input("Text: ")
	if not data:
		break
	else:
		s.send(data)
		print "sent message:", data
s.close()

