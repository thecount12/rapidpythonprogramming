#!/usr/bin/python
#pform.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming

# libs
import cgi,cgitb

form=cgi.FieldStorage()
#get data from fields
firstname=form.getvalue('fname')
lastname=form.getvalue('lname')


print "Content-type:text/html\n\n"
print """
<html>
<h1>Entries from form</h1>
<p>First name is: %s
<p>Last name is: %s
<hr>
</html>
""" % (firstname,lastname)

