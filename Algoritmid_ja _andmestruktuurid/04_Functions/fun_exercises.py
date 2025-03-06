"""Function example"""


# func()
def func():
    """Print to console - I´m inside the function"""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """
    Print to console - My name is [name]

    :param name: name you want to use
    """
    # my_name_is("What is your name?" + name)
    print(f"My name is {name}")


def sum_six(num: int):
    """
    Print to console - Sum of six
    :param num: number to use
    :return: result of 6 + num
    """
    pass
    print(f"sum of six is {num}")


def sum_numbers(num_a, num_b: int):
    """
    Print to console - Sum of numbers
    :param num_a: first number to use
    :param num_b: second number to use
    :return: sum of numbers
    """
    num_a + num_b
    print(f"sum of numbers is: {sum}")


def usd_to_eur(num: int):
    """
    Print to console - USD to Euro
    :param num: number to use
    :return: to Euro
    """
    # print(f"USD to Euro is {num}")
    return print((f"USD to Euro is {num}") * 0, 8)


if __name__ == "__main__":
    func()
    my_name_is("Jelena")
    my_name_is("Merlin")
    sum_six(5)
    sum_numbers(5, 6)
    usd_to_eur(100)


def can_divide():
    my_number = 6
    divides_by_two = False
    divides_by_three = False

    if my_number % 2 == 0:  # Can divide by two?
        divides_by_two = True
    elif my_number % 3 == 0:  # Can divide by three?
        divides_by_three = True

    return divides_by_two, divides_by_three


print(can_divide())
