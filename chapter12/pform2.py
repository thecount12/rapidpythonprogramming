"""
pform.py
Chapter 12 CGI, WSGI Framework Development
Author: William C. Gunnells
Rapid Python Programming
"""


# lib
import cgi

# form=cgi.FieldStorage()
# get data from fields

mypass = "jppass"


def web_page(username, password):
    print("""
    <html>
    <h1>Entries from form</h1>
    <p>First name is: %s
    <p>Last name is: %s
    <hr>
    </html>
    """ % (username, password))


def login():
    print("Content-type:text/html\n\n")
    form = cgi.FieldStorage()
    if form.key("username") and form.key("password"):
        token = form["password"].value
        if token == mypass:
                web_page(form["username"].value, form["password"].value)
        else:
                print("<h1>Wrong username or password!!!</h1>")


login()



