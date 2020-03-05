#!/usr/bin/python
#pform.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import cgi,cgitb

#form=cgi.FieldStorage()
#get data from fields

mypass="jppass"

def webpage(username,password):
        print """
        <html>
        <h1>Entries from form</h1>
        <p>First name is: %s
        <p>Last name is: %s
        <hr>
        </html>
        """ % (username,password)



def login():
        print "Content-type:text/html\n\n"
        form=cgi.FieldStorage()
        if form.has_key("username") and form.has_key("password"):
                token=form["password"].value
                if (token==mypass):
                        webpage(form["username"].value,form["password"].value)
                else:
                        print "<h1>Wrong username or password!!!</h1>"
login()



