"""
gen1.py
Chapter 7 Cool Features of Python
Author: William C. Gunnells
Rapid Python Programming
"""


def mygen():
    print("generate")
    yield 1
    print("my")
    yield 2
    print("list")


if __name__ == "__main__":
    print(mygen())
