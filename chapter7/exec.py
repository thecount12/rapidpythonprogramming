"""
exec.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


code = """
def foo(x): 
    return x+1

print('hello world.')
"""

exec(code)
print(foo(3))




