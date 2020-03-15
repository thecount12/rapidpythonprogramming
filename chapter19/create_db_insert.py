"""
create a quick db and insert some data.
"""

import sqlite3

con = sqlite3.connect('todo.db')
cur = con.cursor()
cur.execute('CREATE TABLE todo (id INTEGER PRIMARY KEY, title VARCHAR(30), description VARCHAR(60))')
con.commit()  # comment back
cur.execute('INSERT INTO todo (id, title, description) VALUES(NULL, "Mow Lawn", "lawn mower, gas, rake, bag grass")')
cur.execute('INSERT INTO todo (id, title, description) VALUES(NULL, "Water Plants", "water hose, water bucket")')
con.commit()

cur.execute('SELECT * FROM todo')
print(cur.fetchall())
