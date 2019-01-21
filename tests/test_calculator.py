import unittest
from calc.calculator import Calculator


class TestCalculator(unittest.TestCase):
    calculator = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertNotEqual(-4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))
        self.assertEqual(-6, self.calculator.add(-3, -3))

    def test_sub(self):
        self.assertEqual(2, self.calculator.sub(3, 1))
        self.assertEqual(0, self.calculator.sub(-3, -3))
        self.assertEqual(-2, self.calculator.sub(1, 3))

    def test_mul(self):
        self.assertEqual(12, self.calculator.mul(3, 4))
        self.assertEqual(0, self.calculator.mul(3, 0))
        self.assertEqual(13.5, self.calculator.mul(3, 4.5))

    def test_div(self):
        self.assertEqual(3, self.calculator.div(9, 3))
        self.assertEqual(4, self.calculator.div(16, 4))


if __name__ == "__main__":
    unittest.main()
