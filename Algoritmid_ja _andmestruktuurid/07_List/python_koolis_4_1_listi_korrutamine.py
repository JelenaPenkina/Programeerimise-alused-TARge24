''' Koosta vähemalt kümnest elemendist koosnev järjend arvudest.
    Koosta programm, mis küsib kasutajalt tegurit ja
    korrutab kõik algses järjendis olnud arvud sellega läbi ning
    väljastab tulemuse ekraanile.

    Sisesta tegur: 3
    45 * 3 = 135
    7 * 3 = 21
    ...
    267 * 3 = 801
'''


def print_multiplications(numbers: list, multiplier: int) -> None:
    # pass  # Kirjutatakse selleks, et ei tekiks syntaxi viga
    for number in numbers:
        print(f"{number} * {multiplier} = {number * multiplier}")


if __name__ == '__main__':
    number = int(input('Sisesta tegur: '))
    print_multiplications([5, 6, 7, -100, 8, 9, 10], number)
