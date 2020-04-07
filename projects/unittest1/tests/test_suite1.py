# coding=utf-8
import unittest
from test_mathfunc import TestMathFunc
from unittest1_tests import MainTest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide"), MainTest("test_add1")]
    suite.addTests(tests)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)