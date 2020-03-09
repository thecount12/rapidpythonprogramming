"""
tcps2.py
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import socket

HOST = '127.0.0.1'                 
PORT = 8001              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
data = conn.recv(1024)
conn.send('Acknowledge'.encode())
print(data)
conn.close()

