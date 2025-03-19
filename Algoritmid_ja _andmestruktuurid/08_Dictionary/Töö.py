"""
Ül 6
1.    Kasutajalt küsitakse sõna.
2.    Kasutajalt küsitakse numbrit.
3.    Loo järjend, kus antud sõna on korrutatud kasvavalt kuni antud numbrini
(kordus, järjend).
4.    Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
5.    Kuva järjendi viimane väärtus
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


#  parem variant def exercise_six():
#     """
#     Küsi kasutajalt sõna ja number.
#
#     Lisa sõna järjendisse vastavalt sisestaud numbrile
#     ("Tere", 3) => ["Tere", "TereTere", "TereTereTere"]
#     Kui number on suurem kui 10 siis prindi "Viga" kui väiksem siis järjendi
#     viimane väärtus
#     """
#     result = []
#     input_string = input('Sisesta üks sõna: ')
#     input_repeat = int(input('Sisesta üks arv: '))
#     if input_repeat > 10:
#         print('Viga')
#     else:
#         for i in range(input_repeat):
#             result.append(input_string * (i + 1))
#         print(result[-1])

if __name__ == '__main__':
    exercise_six()