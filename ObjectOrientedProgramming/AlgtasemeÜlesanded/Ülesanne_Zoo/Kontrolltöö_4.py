"""
Ül 4.

Küsi kasutaja sugu ja vanus
Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
Salvesta järjendisse iga kolmas tervitus ja viimane
Kuva ekraanile järjendis olevate tervituste eelviimased sõnad
"""


def exercise4():
    """
    Ask for the user gender and age
    Use age-appropriate greetings for both men and women.
    Repeat the greeting with increasing age until the greeting changes or 10 times.
    Save every third greeting and the last one in the sequence.
    The penultimate words of the greetings in the sequence on the screen.

    :param: String(tervitus) to be checked
    :return: String greeting.
    """
    gender = input("Sisesta oma sugu (M/N): ")

    while gender not in ["M", "N"]:
        print("Palun sisesta kas 'M' või 'N'!")
        gender = input("Sisesta oma sugu (M/N): ").strip().lower()

    while True:
        try:
            age = int(input("Sisesta oma vanus: "))
            break
        except ValueError:
            print("Palun sisesta kehtiv arv!")

    tervitused = input("Sisesta tervituses: ")
    if gender == "M":
        tervitused = ["Tere, noormees!", "Tere, härrasmees!", "Tere, auväärne mees!"]
    else:
        tervitused = ["Tere, noor daam!", "Tere, proua!", "Tere, auväärne naine!"]

    salvesta_tervitus = []
    eelmine_tervitus = None

    for i in range(10):
        age += 1
        if age < 25:
            greeting = tervitused[0]
        elif age < 40:
            greeting = tervitused[1]
        else:
            greeting = tervitused[2]

        print(greeting)

        if eelmine_tervitus and eelmine_tervitus != greeting:
            break

        if (i + 1) % 3 == 0 or i == 9:
            salvesta_tervitus.append(greeting)

    print("Save every third greeting:")
    for greeting in salvesta_tervitus:
        words = greeting.split()
        if len(words) > 1:
            print(words[-2])


if __name__ == '__main__':
    exercise4()
