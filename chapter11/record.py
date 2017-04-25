#!/usr/bin/python
#record.py
# list information in table
# Chapter 11 Sockets and Dabases 
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import sqlite3

con=sqlite3.connect('user.db')
cur=con.cursor()
cur.execute('SELECT * FROM userinfo')
print cur.fetchall()
