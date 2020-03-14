import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock


class TestMagic(unittest.TestCase):

    def test_1(self):
        self.foo = MagicMock()

    def test_2(self):
        bar = Mock()
        bar.__len__ = Mock(return_value=1)
        print(len(bar))
        pass

    def test_3(self):
        self.foo = MagicMock(return_some_number=42)
        self.foo.method(3, 4, 5, key='value')
        self.foo.method.assert_called_with(3, 4, 5, key='value')


