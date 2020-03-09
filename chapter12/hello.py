"""
hello.py
Chapter 12 CGI, WSGI Framework Development
Author: William C. Gunnells
Rapid Python Programming
"""


# libs
from wsgiref.simple_server import make_server
from urllib.parse import urlparse


def hello(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    par = urlparse(environ.get('QUERY_STRING', ''))
    if 'a_name' in par[2]:
        a_name = par[2].replace("aname=", "")
        print(f"example: {a_name}")
    else:
        a_name = 'World'
    return [b'''<p>Hello %s!</p>''' % a_name.encode()]


if __name__ == '__main__':
    srv = make_server('localhost', 8080, hello)
    srv.serve_forever()

