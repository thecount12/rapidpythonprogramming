"""
create.py
create user.db
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import sqlite3 

con = sqlite3.connect('user.db')
cur = con.cursor()
cur.execute('CREATE TABLE userinfo (id INTEGER PRIMARY KEY, fname VARCHAR(20), lname VARCHAR(30))')
con.commit()  # comment back
cur.execute('INSERT INTO userinfo (id, fname, lname) VALUES(NULL, "john", "doe")')
con.commit()

cur.execute('SELECT * FROM userinfo')
print(cur.fetchall())


