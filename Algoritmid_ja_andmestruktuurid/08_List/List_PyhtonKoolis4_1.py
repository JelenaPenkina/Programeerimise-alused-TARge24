"""
Koosta vähemalt kümnest elemendist koosnev järjend arvudest. Koosta programm,
mis küsib kasutajalt tegurit ja korrutab kõik algses järjendis olnud arvud
sellega läbi ning väljastab tulemuse ekraanile.

Sisesta tegur: 3
45 * 3 = 135
7 * 3 = 21
...
267 * 3 = 801
"""


def multiply_elements(numbers: list, multiplier: int):
    for i in range(len(numbers)):
        print(f'{multiplier} * {numbers[i]} = {multiplier * numbers[i]}')


if __name__ == '__main__':
    multiplier = int(input('Sisesta tegur '))
    multiply_elements([11, 2, 3, 4, 5, 21, 43, 65, 34, 12, 76, 43, 134, -123],
                      multiplier)