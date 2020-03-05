#!/usr/bbin/python
#first.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming

# libs 
from cgi import * 

def hello(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''<p>Hello World, and good day!!!</p>''']

if __name__ =="__main__":
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello)
    srv.serve_forever()

