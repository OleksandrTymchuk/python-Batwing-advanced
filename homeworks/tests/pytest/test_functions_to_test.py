from functions_to_test import Calculator
import pytest


def test_add():
    assert Calculator.add(11, -2) == 9
    assert Calculator.add(100, 3) == 103


def test_subtract():
    assert Calculator.subtract(3, -13) == 16
    assert Calculator.subtract(50, 50) == 0


def test_multiply():
    assert Calculator.multiply(0, 1) == 0
    assert Calculator.multiply(-5, 100) == -500


def test_divide():
    assert Calculator.divide(100, -1) == -100
    with pytest.raises(ValueError):
        assert Calculator.divide(1, 0)