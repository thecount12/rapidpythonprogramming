"""
pform.py
Chapter 12 CGI, WSGI Framework Development
Author: William C. Gunnells
Rapid Python Programming
"""


# libs
import cgi

form = cgi.FieldStorage()
# get data from fields
first_name = form.getvalue('fname')
last_name = form.getvalue('lname')


print("Content-type:text/html\n\n")
print("""
<html>
<h1>Entries from form</h1>
<p>First name is: %s
<p>Last name is: %s
<hr>
</html>
""" % (first_name, last_name))

