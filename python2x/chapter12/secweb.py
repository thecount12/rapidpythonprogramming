#!/usr/bin/python
#secweb.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming


print 'Content-type: text/html\n\n'

var="Hello world"
print """
<html><head>
<title>Second Web Page</title>
</head><body>
<h1> Messasge to you: %s</h1>
</body>
</html>
""" % var

