from unittest1 import main
import unittest


class MainTest(unittest.TestCase):
    def test_main(self):
        self.assertEqual(3, main.add(1, 2))
