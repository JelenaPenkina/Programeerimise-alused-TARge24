def banner(slogan: str) -> str:
    """Enter advertising slogan."""
    print(slogan.upper())


def repeat_banner():
    """Repeat slogan as many times as users inserts."""
    repeat_time = int(
        input('Enter number of times You want to repeat slogan: '))
    slogan = input('Enter advertising slogan: ')
    while repeat_time > 0:
        banner(slogan)
        repeat_time -= 1


if __name__ == '__main__':
    repeat_banner()
