# coding=utf-8

import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner as html

if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestMathFunc("test_add"),TestMathFunc("test_minus"), TestMathFunc("test_divide")]

    suite.addTests(tests)

    with open('HTMLReport.html', 'w') as f:
        runner = html.HTMLTestRunner(stream=f, title='MathFunc Test Report', description='generated by HTMLTestRunner.',
                                     verbosity=2)
        runner.run(suite)