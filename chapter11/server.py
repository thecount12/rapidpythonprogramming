"""
server.py
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from socket import *

host = "localhost"
port = 8001 
buf = 1024
addr = (host,port)

u = socket(AF_INET, SOCK_DGRAM)
u.bind(addr)

while 1:
    data, addr = u.recvfrom(buf)
    if not data:
        break
    else:
        print("Received message:", data.decode())

u.close()


