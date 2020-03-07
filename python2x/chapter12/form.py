#!/usr/bin/python
#form.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming


print "Content-type:text/html\n\n"
print """
<html>
<form action="pform.py" method="get">
First Name: <input type="text" name="fname">  <br />

Last Name: <input type="text" name="lname" />
<input type="submit" value="Submit" />
</form>
"""



