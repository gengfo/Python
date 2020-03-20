import unittest
from SimpleCalc import main as main


class TestAddFunc(unittest.TestCase):
    def setUp(self):
        print("setUp triggered")

    def tearDown(self):
        print("teardown triggered")

    def testAdd(self):
        print("test add")
        self.assertEqual(3, main.add(1, 2))
        self.assertNotEqual(4, main.add(1, 2))
        # self.assertNotEqual(3, add(2, 2))
