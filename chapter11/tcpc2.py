#!/usr/bin/python
#tcpc2.py
# Chapter 11 Sockets and Dabases 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import socket

HOST = 'localhost'    
PORT = 8001              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')  
data = s.recv(1024)       
s.close()                 
print 'Received', repr(data)
