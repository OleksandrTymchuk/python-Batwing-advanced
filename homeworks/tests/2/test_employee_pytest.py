from employee import Employee
import pytest


otymchuk = Employee('Oleksandr', 'Tymchuk', 500)


def test_mail():
    assert otymchuk.email == 'Oleksandr.Tymchuk@email.com'


def test_fullname():
    assert otymchuk.fullname == 'Oleksandr Tymchuk'


def test_apply_raise():
    assert otymchuk.pay*otymchuk.raise_amt == 525
