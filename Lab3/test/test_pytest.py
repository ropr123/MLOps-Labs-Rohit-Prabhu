from src.calculator import addition, subtraction, multiplication, division, factorial


def test_addition():
    assert addition(2, 3) == 5


def test_subtraction():
    assert subtraction(7, 4) == 3


def test_multiplication():
    assert multiplication(3, 5) == 15


def test_division():
    assert division(8, 2) == 4


def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
