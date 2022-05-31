import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(10, 2), 12)
        self.assertEqual(Calculator.add(0, 3), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(11, -2), 13)
        self.assertEqual(Calculator.subtract(12, 3), 9)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(11, -2), -22)
        self.assertEqual(Calculator.multiply(12, 3), 36)

    def test_divide(self):
        self.assertEqual(Calculator.divide(12, -2), -6)
        self.assertRaises(ValueError, Calculator.divide, 11, 0)
        