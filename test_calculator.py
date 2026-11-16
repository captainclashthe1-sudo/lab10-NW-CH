# https://github.com/captainclashthe1-sudo/lab10-NW-CH
# Partner 1: Eric Castro
# Partner 2: Jackson Kokinda

import math
import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(7, 2), 5)
        self.assertEqual(calculator.subtract(2, 7), -5)

    def test_multiply(self):
        self.assertEqual(calculator.mul(4, 5), 20)
        self.assertEqual(calculator.mul(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(-3, 12), -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 10)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(16), 4)
        self.assertAlmostEqual(calculator.square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


if __name__ == "__main__":
    unittest.main()
