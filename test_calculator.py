
import unittest
import math
import calculator


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 5), 20)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

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
