#!/usr/bin/pythyon 
#hello.py
# Chapter 12 CGI, WSGI Framework Development
# Author: William C. Gunnells
# Rapid Python Programming

# libs
from cgi import * 

def hello(environ, start_response):
    par= parse_qs(environ.get('QUERY_STRING', ''))
    if 'aname' in par:
        aname= escape(par['aname'][0])
    else:
        aname= 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''<p>Hello %(aname)s!</p>''' % {'aname':aname}]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello)
    srv.serve_forever()

