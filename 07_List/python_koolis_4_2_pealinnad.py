'''
    Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

    Väljasta linnad eraldi ridadena.
    Järjesta need tähestikulisse järjekorda.
    Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
    Esita linnade nimed tähestikulises järjekorras, lisades iga nime ette ka järjekorra numbri.
    Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
    kus linnade arv leitakse vastava funktsiooni abil.
'''


def print_list(capitols, numbered=False):
    for number, name in enumerate(capitols):
        if numbered:
            print(f"{number + 1}. {name}")
        else:
            print(f"{name}")
        # list_of_capitols.sort()


if __name__ == '__main__':
    capitols = ["Tallinn", "Riia", "Helsinki", "Stockholm", "Vilnius",
                "Varssav", "Brüssel", "Pariis", "Lissabon", "Berlin"]
    print_list(capitols)
    # TODO sorteeri ja lisa kaks
    capitols.sort()
    print_list(capitols, numbered=True)
    # TODO prindi kokkuvõte
