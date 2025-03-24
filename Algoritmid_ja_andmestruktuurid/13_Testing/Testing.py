import math

import pytest


def solve_quadratic_equation(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    if a == 0:
        return -(c / b),

    disc = b ** 2 - 4 * a * c
    if disc < 0:
        return None
    if disc == 0:
        return -b / (2 * a),
    x1 = (-b - math.sqrt(disc)) / (2 * a)
    x2 = (-b + math.sqrt(disc)) / (2 * a)
    return x1, x2


def test__solve_quadratic_equation__two_solutions():
    assert solve_quadratic_equation(2, 6, -20) == (-5.0, 2.0)


def test__solve_quadratic_equation__two_float_solutions():
    x1, x2 = solve_quadratic_equation(2, 3, -57)
    assert (round(x1, 3), round(x2, 3)) == (-6.141, 4.641)


def test__solve_quadratic_equation__single_float_solutions():
    assert solve_quadratic_equation(1, -6, 9) == (3, 3)


def test__solve_quadratic_equation__no_solutions():
    with pytest.raises(ValueError) as e_info:
        solve_quadratic_equation(2, 6, 10)
        assert str(e_info.value) == "math domain error"


def test__solve_quadratic_equation__zero_division():
    with pytest.raises(ZeroDivisionError) as e_info:
        solve_quadratic_equation(0, 6, 10)
        assert str(e_info.value) == "float division by zero"
        # assert e_info.tb.tb_lineno == 32


def test_normal_values():
    assert solve_quadratic_equation(1, -3, 2) == (1, 2)


def test_integer_values():
    assert solve_quadratic_equation(1, -3, 2) == (1, 2)


def test_float_values():
    assert solve_quadratic_equation(1, -4, 3.75) == (1.5, 2.5)


def test_one_solution():
    assert solve_quadratic_equation(1, -4, 4) == (2,)


def test_no_solution():
    assert solve_quadratic_equation(1, 1, 1) == None


def test_linera_equation():
    assert solve_quadratic_equation(0, 1, 1) == (-1,)
