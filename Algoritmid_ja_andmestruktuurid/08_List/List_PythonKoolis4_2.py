"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka
järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
kus linnade arv leitakse vastava funktsiooni abil.
"""


def print_list(capitals, numbered=False):
    for number, capital in enumerate(capitals):
        if numbered:
            print(f'{number + 1}. {capital}')
        else:
            print(capital)


if __name__ == '__main__':
    capitols = ['Tallinn', 'Riga', 'Helsinki', 'Vilnius', 'Berlin', 'Stockholm',
                'Paris', 'Lissabon', 'Brüssel', 'Varssav']
    print_list(capitols)

    for i in range(2):
        new_capitols = input(f'Sisesta {i + 1}. lisa pealinn')
        capitols.append(new_capitols)
    capitols.sort()
    print_list(capitols, numbered=True)
    print(f'Meie järjendis on {len(capitols)} euroopa pealinna')