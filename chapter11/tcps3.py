"""
tcps3.py
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import socket

HOST = '127.0.0.1'                 
PORT = 8001              
s = socket.socket()
s.bind((HOST, PORT))
s.listen(2)
conn, addr = s.accept()
print('Connected by', str(addr))
while True:
    data = conn.recv(1024).decode()
    # if not data:
    #     break
    print("from connected user: " + str(data))
    data = input(' -> ')
    conn.send(data.encode())
conn.close()

