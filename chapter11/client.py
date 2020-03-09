"""
client.py
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

u = socket(AF_INET,SOCK_DGRAM)

msg = "Send messages to server: "
print("Message sent:", msg)

while True:
    data = input('Text: ')
    if not data:
        break
    else:
        if u.sendto(data.encode(), addr):
            print("send message:", data)

u.close()

