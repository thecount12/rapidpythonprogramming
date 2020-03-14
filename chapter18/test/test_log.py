"""
unittest and test log
"""

import logging
import unittest
import sys
from project.basic_program import Basic

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class DebugBasic(unittest.TestCase):

    def setUp(self) -> None:
        self.func = Basic(2, 3)
        logger.info("boom")

    def test_1(self):
        logger.info(f"print anything: {self.func.add()}")


if __name__ == "__main__":
    unittest.main()
