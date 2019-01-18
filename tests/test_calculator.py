import unittest
from calc.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    calculator = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calculator.add(2, 2))
        self.assertEqual(3.2, self.calculator.add(1, 2.2))

    def test_minus(self):
        self.assertEqual(2, self.calculator.sub(3, 1))
        self.assertEqual(-2, self.calculator.sub(1, 3))

    def test_multiple(self):
        self.assertEqual(12, self.calculator.mul(3, 4))
        self.assertEqual(13.5, self.calculator.mul(3, 4.5))

    def test_devide(self):
        self.assertEqual(3, self.calculator.div(9, 3))
        self.assertEqual(4, self.calculator.div(16, 4))


if __name__ == "__main__":
    unittest.main()
