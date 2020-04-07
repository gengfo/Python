from unittest1 import main
import unittest


class MainTest(unittest.TestCase):
    def setUp(self):
        print ('setUp MainTest...')

    def tearDown(self):
        print ('tearDown MainTest...')

    def test_add1(self):
    	self.assertEqual(3, main.add(1, 2))

    def test_add2(self):
    	self.assertNotEqual(4, main.add(1, 2))