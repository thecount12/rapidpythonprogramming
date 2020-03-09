"""
first.py
Chapter 12 CGI, WSGI Framework Development
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
from wsgiref.simple_server import make_server


def hello(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)

    return [b'''<p>Hello World, and good day!!!</p>''']


if __name__ == "__main__":
    srv = make_server('localhost', 8080, hello)
    srv.serve_forever()

