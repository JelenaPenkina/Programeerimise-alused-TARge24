import pytest
from setuptools.command.egg_info import egg_info


def solve_quadratic_equation(a, b, c):
    """
    Solving quadratic equation
    ax^2 + bx + c = 0
    :param a: ax^2
    :param b: bx
    :param c: c
    :return: (x1, x2) tuple
    """
    disc = b**2 - 4 * a * c
    import math
    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)
    return x1, x2

def test__solve_quadratic_equation__two_solutions():
    assert solve_quadratic_equation(2,6,-20) == (-5.0, 2.0)

def test__solve_quadratic_equation__two_float_solutions():
    x1, x2 = solve_quadratic_equation(2.0,3,-57)
    assert (round(x1, 3), round(x2, 3)) == (-6.141, 4.641)

def test__solve_quadratic_equation__single_float_solutions():
    assert solve_quadratic_equation(1,-6,9) == (3,3)

def test__solve_quadratic_equation__no_solutions():
    with pytest.raises(ValueError) as e_info:
        solve_quadratic_equation(2,6,10)
    assert str(e_info.value) == "Math domain error"

def test__solve_quadratic_equation__zero_division():
    with pytest.raises(ZeroDivisionError) as e_info:
        solve_quadratic_equation(0,6,10)
    assert str(e_info.value) == "float division by zero"