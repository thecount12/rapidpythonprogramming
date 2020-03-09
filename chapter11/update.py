"""
update.py
list information in table
Chapter 11 Sockets and Dabases
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import sqlite3

con = sqlite3.connect('user.db')
cur = con.cursor()
cur.execute("update userinfo set lname='bob' where fname='george'") 
con.commit()
cur.execute('SELECT * FROM userinfo')
print(cur.fetchall())
cur.close()
con.close()
