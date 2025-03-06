"""Function examples."""


# func()
def func():
    """Print to console - I´m inside the function."""
    print("I´m inside the function")


# my_name_is(name)
def my_name_is(name: str) -> None:
    """
    Print to console - My name is [name].
    :param name: name you want to use.
    """
    # my_name_is("What is your name?" + name)
    print(f"My name is {name}")


# sum_six(num)
def sum_six(num: int):
    """
    Print to console - Sum of six.
    :param num: number to use.
    :return: result of 6 + num.
    """
    pass
    print(f"sum of six is {num}")
    return 6 + num


# sum_numbers()
def sum_numbers(num_a, num_b: int):
    """
    Print to console - Sum of numbers.
    :param num_a: first number to use.
    :param num_b: second number to use.
    :return: sum of numbers.
    """
    num_a + num_b
    print(f"sum of numbers is: {sum}")
    return num_a + num_b


# usd_to_eur()
def usd_to_eur(num: int):
    """
    Print to console - USD to Euro.
    :param num: number to use.
    :return: to Euro.
    """
    # print(f"USD to Euro is {num}")
    # return print((f"USD to Euro is {num}") * 0.8)
    return num * 0.8
