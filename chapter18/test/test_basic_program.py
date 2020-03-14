"""
unittest for basic program
"""

import unittest
from project.basic_program import Basic


class TestAssert(unittest.TestCase):

    def test(self):  # assert works
        self.assertTrue(True)


class TestBasic(unittest.TestCase):

    def setUp(self) -> None:
        self.func = Basic(2, 2)

    def test_1(self):
        self.assertEqual(self.func.multiply(), 4)

    def test_2(self):
        self.assertEqual(self.func.add(), 4)

    def test_3(self):
        self.assertIsInstance(self.func.multiply(), int)

    def test_4(self):
        self.assertIsInstance(self.func.report(), str)

    def test_5(self):
        self.assertIsInstance(self.func.combine(), tuple)


if __name__ == "__main__":
    unittest.main()
