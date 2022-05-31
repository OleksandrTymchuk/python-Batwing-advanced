import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.data = Employee("Oleksandr", "Tymchuk", 500)

    def test_email(self):
        self.assertEqual(self.data.email, "Oleksandr.Tymchuk@email.com")

    def test_fullname(self):
        self.assertEqual(self.data.fullname, "Oleksandr Tymchuk")

    def test_apply_raise(self):
        self.data.apply_raise()
        self.assertEqual(self.data.pay, 525)

