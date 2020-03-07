"""
raise4.py
Chapter 5 Exceptions
Author: William C. Gunnells
Rapid Python Programming
"""

import sys


def lets_error():
    raise RuntimeError('Force the error')


def main(num):
    try:
        if num < 3:
            lets_error()
        else:
            blah = num * num
            print("my number is", blah)
    except Exception as err:
        sys.stderr.write("%s your number %s is less than 3\n" % (str(err), num))
    finally:
        print("okay, I could close the file or end this et...")


main(2)
