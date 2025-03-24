"""
Funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:

•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu

"""

filename = input("Sisesta faili nimi: ")


def female_average():
    """
    print female average.
    """
    n_average = round(total_n / count_n)
    if n_average > 2600:
        print(f'N {n_average}m, väga hea')
    elif n_average > 1800:
        print(
            f'N {n_average}m, rahuldav, järgmist hindest puudu {2600 - n_average}m ')
    else:
        print(
            f'N{n_average}m, nõrk, järgmist hindest puudu {1800 - n_average}m ')


def male_average():
    """
    print male average.
    """
    m_average = round(total_m / count_m)
    if m_average > 2800:
        print(f'M {m_average}m, väga hea')
    elif m_average > 2000:
        print(
            f'M {m_average}m, rahuldav, järgmist hindest puudu {2800 - m_average}m ')
    else:
        print(
            f'M {m_average}m, nõrk, järgmist hindest puudu {2000 - m_average}m ')


def female_results():
    """
    print female results.
    """
    if k >= 2600:
        print(f'{v} {k}m, väga hea')
    elif k < 1800:
        print(f'{v} {k}m, nõrk, järgmist hindest puudu {1800 - k}m')
    else:
        print(f'{v} {k}m, rahuldav, järgmist hindest puudu {2600 - k}m')


def male_results():
    """
    print male results.
    """
    if k >= 2800:
        print(f'{v} {k}m, väga hea')
    elif k < 2000:
        print(f'{v} {k}m, nõrk, järgmist hindest puudu {2000 - k}m')
    else:
        print(f'{v} {k}m, rahuldav, järgmist hindest puudu {2800 - k}m')


with open(filename + ".txt") as f:
    data = [line.strip().split() for line in f]
    data_filter = [(int(meters), gender) for meters, gender in data]
    total_n = 0
    total_m = 0
    count_n = 0
    count_m = 0
    for k, v in data_filter:
        if v == 'N':
            count_n += 1
            total_n += k
            female_results()
        else:
            count_m += 1
            total_m += k
            male_results()
    print('Keskmised:')
    male_average()
    female_average()