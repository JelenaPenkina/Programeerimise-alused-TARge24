"""
Ül 6
1.Kasutajalt küsitakse sõna.
2.Kasutajalt küsitakse numbrit.
3.Loo järjend, kus antud sõna on korrutatud kasvavalt kuni antud numbrini
(kordus, järjend).
4.Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
5.Kuva järjendi viimane väärtus
"""


def exercise_six():
    """
    Küsi kasutajalt sõna ja number.

    Lisa sõna järjendisse vastavalt sisestaud numbrile
    ("Tere", 3) => ["Tere", "TereTere", "TereTereTere"]
    Kui number on suurem kui 10 siis prindi "Viga" kui väiksem siis järjendi
    viimane väärtus
    """
    result = []
    input_string = input('Sisesta üks sõna: ')
    while True:
        try:
            input_repeat = int(input('Sisesta üks arv: '))
        except ValueError:
            print('Siseta palun ainult numbreid')
        else:
            break
    if input_repeat > 10:
        print('Viga')
    else:
        for i in range(input_repeat):
            result.append(input_string * (i + 1))
        print(result[-1])


if __name__ == '__main__':
    exercise_six()


def exercise_six2():
    """
    1.1 Küsi kasutajalt sõna.
    1.2 Küsi kasutajalt number.
    1.3 Loo järjend, kus sõna korrutatakse kasvavalt kuni antud numbrini.
    1.4 Kui number on suurem kui 10, väljasta "Viga".
    1.5 Kuvatakse järjendi viimane väärtus.
    """
    # 1.1 Küsi sõna
    sona = input("Sisesta üks sõna: ")

    # 1.2 Küsi number ja kontrolli, kas see on kehtiv
    while True:
        try:
            number = int(input("Sisesta üks arv: "))
            break
        except ValueError:
            print("Palun sisesta kehtiv number!")

    # 1.4 Kontrolli, kas number on suurem kui 10
    if number > 10:
        print("Viga")
    else:
        # 1.3 Loo järjend, kus sõna korrutatakse kasvavalt
        jarjend = [sona * (i + 1) for i in range(number)]

        # 1.5 Kuvatakse järjendi viimane väärtus
        print("Viimane väärtus järjendis:", jarjend[-1])


if __name__ == "__main__":
    exercise_six2()