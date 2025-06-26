import unittest
from pymath.lib.math import factorial, fibonacci, gcd, lcm, is_perfect_square

class TestMath(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)

    def test_lcm(self):
        self.assertEqual(lcm(48, 18), 144)
        self.assertEqual(lcm(101, 103), 10403)

    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(0))
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(144))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(10))
        self.assertFalse(is_perfect_square(-1))

if __name__ == '__main__':
    unittest.main()
