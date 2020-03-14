"""
foo test
"""

import unittest


def add(x, y):
    return x + y


class MyFirstTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(2, 3), 5)


def test_add():
    assert add(2, 3) == 4
