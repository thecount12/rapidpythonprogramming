#!/usr/bin/python
#tcps4.py
# Chapter 11 Sockets and Dabases 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import socket

HOST = '127.0.0.1'                 
PORT = 8001              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
	data= conn.recv(1024)
	if not data: break
	conn.send(data)
	print "sent: " , data
conn.close()

