"""
Koostada funktsioon, mis võtab argumentideks vaiba lõpp-pikkuse (ujukomaarv) ja lõimede arvu (täisarv),
•	arvutab ja tagastab vaiba lõimede kogupikkuse ümardatuna sajandikeni.
Koostada programm, mis
•	küsib kasutajalt
o	failinime, kus on vaipade lõpp-pikkused ujukomaarvudena meetrites eraldi ridadel,
o	kõrvuti olevate lõimede arvu 5-meetriste ja pikemate vaipade puhul (täisarv),
o	kõrvuti olevate lõimede arvu lühemate vaipade puhul (täisarv);
•	loeb failist vaipade pikkused,
•	arvutab (funktsiooni abil) ja väljastab ekraanile iga vaiba lõimede kogupikkuse,
•	arvutab ja väljastab ekraanile, kui palju läheb lõimeniiti vaja kõigi vaipade peale kokku ümardatuna sajandikeni.

"""

from cooper.cooper_vol2 import read_file

DEFAULT_FILE_NAME = 'delta_vaibad.txt'
LONG_RUG = 5
with open(DEFAULT_FILE_NAME, 'w', encoding='utf8') as f:
    f.write("""7
4.9
3.63
5
""")


def calculate_thread_length(rug_final_length: float,
                            thread_count: int) -> float:
    """
    Calculate length of thread needed for given rug dimensions.

    single thread length - rug_final_length ? 20% + 2 * 0,25
    :param rug_final_length: in meters
    :param thread_count:
    :return: thread_count times single thread length
    """
    single_thread_length = rug_final_length * 1.2 + 0.5
    return round(single_thread_length * thread_count, 2)


if __name__ == '__main__':
    filename = input(f'Sisesta failinimi [{DEFAULT_FILE_NAME}]: ')
    long_rug_thread_count = int(input(
        f'Sisestage {LONG_RUG}-meetriste ja pikemate vaipade lõimede arv '))
    short_rug_thread_count = int(
        input(f'Sisestage lühemate vaipade lõimede arv '))
    rug_lengths = read_file(filename if filename else DEFAULT_FILE_NAME)
    total_thread_length = 0
    for length_txt in rug_lengths:
        rug_length = float(length_txt)
        if rug_length >= LONG_RUG:
            thread_length = calculate_thread_length(rug_length,
                                                    long_rug_thread_count)
        else:
            thread_length = calculate_thread_length(rug_length,
                                                    short_rug_thread_count)
        print(f'{length_txt} m vaible kulub {thread_length} m lõime')
        total_thread_length += thread_length
    print(
        f'Kõikide vaipde peale läheb vaja {total_thread_length} meetrit lõimeniiti')