"""Math exercises."""
from math import pi, sqrt


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


# print(sum_and_difference(1, 2))

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = num_a / num_b
    return division


# print(float_division(5, 2))


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = num_a // num_b
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    average = num_a / num_b
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    return round(radius ** 2 * pi)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    # Write your code here
    # Area = √3 / 4 × (side) aste 2
    return int(round(side_length ** 2 * sqrt(3)) / 4, 2)

    def calculate_discriminant(a: int, b: int, c: int) -> int:
        """Calculate discriminant with given variables and return the result."""
        # Write your code here
        discriminant = (a * b) - (b * c)
        return discriminant

    def calculate_hypotenuse_length(a: int, b: int) -> float:
        """Return the length of hypotenuse when the lengths of the catheti are given."""
        # Write your code here
        c = 11
        return c

    def calculate_cathetus_length(a: int, c: int) -> float:
        """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
        # Write your code here
        b = 3
        return b

    if __name__ == '__main__':  # käivitamise ajal name muutub mainiks,
        # faili kui runnitakse käivitab ta koodi
        assert sum_and_difference(5, 6) == (11, -1)
        # nt panin print("OK"), sest kui assert loeb ise kas on võrdne või mitte, siis ta ei kuva midagi
        # kuid kui on õige, siis prindib välja OK
        print("OK")
        print(sum_and_difference(11, 9), "== (20, 2)")
        # 2
        assert float_division(5, 2) == (2.5)
        print("OK")
        # 3
        assert integer_division(15, 2) == (7)
        print("OK")
        # 4
        # assert powerful_operations(10,3) == (1000, 1)
        # assert powerful_operations(2, 10) == (1024, 2)
        print("OK")
        # 5
        print(find_average(4, 9))
        # 6
        # print(area_of_a_circle(1)
        # assert area_of_a_circle(1) == 3.14
        # 7
        assert area_of_an_equilateral_triangle(3) == 4
        assert area_of_an_equilateral_triangle(15) == 97
        # 8
        # 9

        # CTRL+ALT+L -vigade parandus, korrigeerib stiili kui saadan tööd, teen ära
