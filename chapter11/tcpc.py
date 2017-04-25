#!/usr/bin/python
#tcpc.py
# Chapter 11 Sockets and Dabases 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import socket

HOST = 'localhost'    
PORT = 8001              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)       
print data
s.close()                 


