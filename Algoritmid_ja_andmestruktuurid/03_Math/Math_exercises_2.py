"""Math exercises vol2."""
import math


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    sine = round(math.sin(math.radians(angle)), 1)
    cosine = round(math.cos(math.radians(angle)), 1)
    return f"Nurk: {angle}, siinus: {sine}, koosinus: {cosine}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string."""
    string_numbers = str(num_a) + str(num_b)
    return string_numbers


if __name__ == '__main__':
    print(time_converter(3600))
    assert time_converter(3660) == "3660 sekundit on 1 tund(i) ja 1 minut(it)."

    print(student_helper(30))
    assert student_helper(30) == 'Nurk: 30, siinus: 0.5, koosinus: 0.9.'

    print(greetings(10))
    assert greetings(3) == "HeyHeyHey"

    print(adding_numbers(110, 201))
    assert adding_numbers(10, 20) == "1020"

    print("OK")


    def print_sum_of_numbers(list_of_numbers):
        print(sum(list_of_numbers))


    print(print_sum_of_numbers([1, 2, 3, 4, 5]))
