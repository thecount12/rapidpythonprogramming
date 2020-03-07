"""
raise.py
Chapter 5 Exceptions
Author: William C. Gunnells
Rapid Python Programming
"""


def lets_error():
    raise RuntimeError('Force the error')


def main():
    lets_error()


main()
