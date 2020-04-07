import unittest

import mathfunc


class TestMathFunc(unittest.TestCase):
    def setUp(self):
        print('setUp TestMathFunc...')

    def tearDown(self):
        print('tearDown TestMathFunc...')

    def test_minus(self):
        self.skipTest('do not run this.')
        self.assertEqual(1, mathfunc.minus(3, 2))

    def test_add(self):
        pass

    # self.assertEqual(3, add(1, 2))
    # self.assertNotEqual(3, add(2, 2))

    def test_multi(self):
        pass

    # self.assertEqual(6, multi(3, 2))

    @unittest.skip("i don't want to run this case.")
    def test_divide(self):
        pass

# self.assertEqual(2, divide(6, 3))
# self.assertEqual(2, divide(4, 2))


if __name__ == '__main__':
    unittest.main()
