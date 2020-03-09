"""
tcpc3.py
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import socket

HOST = 'localhost'    
PORT = 8001              
s = socket.socket()
s.connect((HOST, PORT))
data = input(" -> ")
while data.lower().strip() != 'bye':
    s.send(data.encode())
    dat = s.recv(1024).decode()
    print("sent message:", str(dat))
    data = input(" -> ")
s.close()

