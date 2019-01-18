import unittest
from calc.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(Calculator.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(Calculator.mul(3, 2), 6)

    def test_div(self):
        self.assertEqual(Calculator.div(8, 2), 4)


if __name__ == '__main__':
    unittest.main()
