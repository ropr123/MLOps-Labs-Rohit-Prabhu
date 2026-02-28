import unittest

from src.calculator import addition, subtraction, multiplication, division, factorial


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(7, 4), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(3, 5), 15)

    def test_division(self):
        self.assertEqual(division(8, 2), 4)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
