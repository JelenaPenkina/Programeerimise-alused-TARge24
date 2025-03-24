"""Function examples."""


def func():
    """Print to console - I am inside the function."""
    print("I´m inside the function")


def my_name_is(name: str) -> None:
    """Print to console - my name is [name].

    :param name: name You want to use
    """
    print(f'My name is {name}')


def sum_six(num: int) -> int:
    """
    Print to console - sum of six is [num].

    :param num: number You want to use
    """
    return num + 6


def sum_numbers(number1: int, number2: int) -> int:
    """
    Print to console - sum of numbers is [number1, number2].

    :param number1: number You want to use
    :param number2: number You want to use
    """
    return number1 + number2


def usd_to_eur(amount_in_usd: int) -> float:
    """
    Print to console - amount of euro is [amount_in_usd].

    :param amount_in_usd: amount you want to use
    """
    return amount_in_usd * 0.8


if __name__ == '__main__':
    func()
    my_name_is('Orvet')
    print(sum_six(6))
    print(sum_numbers(5, 5))
    print(usd_to_eur(100))