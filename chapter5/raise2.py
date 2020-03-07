"""
raise2.py
Chapter 5 Exceptions
Author: William C. Gunnells
Rapid Python Programming
"""

import sys


def lets_error():
    raise RuntimeError('Force the error')


def main():
    try:
        lets_error()
    except Exception as err:
        sys.stderr.write(str(err))


main()
