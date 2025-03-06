"""
Koostada funktsioon, mis võtab argumentideks vaiba lõpp-pikkuse (ujukomaarv)
ja lõimede arvu (täisarv),
•	arvutab ja tagastab vaiba lõimede kogupikkuse ümardatuna sajandikeni.

Koostada programm, mis
•	küsib kasutajalt
o	failinime, kus on vaipade lõpp-pikkused ujukomaarvudena meetrites eraldi ridadel,
o	kõrvuti olevate lõimede arvu 5-meetriste ja pikemate vaipade puhul (täisarv),
o	kõrvuti olevate lõimede arvu lühemate vaipade puhul (täisarv);
•	loeb failist vaipade pikkused,
•	arvutab (funktsiooni abil) ja väljastab ekraanile iga vaiba lõimede kogupikkuse,
•	arvutab ja väljastab ekraanile, kui palju läheb lõimeniiti vaja kõigi vaipade
peale kokku ümardatuna sajandikeni.

"""
""" def vaiba_loime_pikkus(lõpp_pikkus, lõimede_arv):
    pindala = lõpp_pikkus *lõimede_arv

    kogupikkus = pindala * lõimede_arv
    kogupikkus = round(kogupikkus, 2)

    return kogupikkus

if __name__ == '__main__':
    print(vaiba_loime_pikkus(5,20))
    print(vaiba_loime_pikkus(15,15)) """

# ÕPETAJA VERSIOON
from Tunnitöö_Cooperi_Test import read_file

default_file_name = "delta_vaibad.txt"
long_rug = 5
with open(default_file_name, "w", encoding="utf8") as file:
    file.write("""7
4.9 
3.63 
5
""")


def calculate_thread_length(rug_final_length: float,
                            thread_count: int) -> float:
    """
    Calculate length of thread needed for given rug dimensions.

    Single thread length - rug_final_length + 20% + 2 * 0,25
    :param rug_final_length: in meters
    :param thread_count:
    :return: thread_count times single thread length
    """
    single_thread_length = rug_final_length * 1.2 + 0, 5
    return round(single_thread_length * thread_count, 2)


if __name__ == '__main__':
    filename = input("Sisestage failinimi:[{default_file_name}] ")
    long_rug_thread_count = int(input(
        f"Sisestage {long_rug} - meetriste ja pikemate vaipade lõimede arv; "))
    short_rug_thread_count = int(
        input("Sisestage lühemate vaaipade lõimede arv: "))
    rug_lengths = read_file(filename if filename else default_file_name)
    total_thread_length = 0
    for length_txt in rug_lengths:
        rug_lengths = float(length_txt)
        if rug_lengths >= long_rug:
            thread_length = calculate_thread_length(rug_lengths,
                                                    long_rug_thread_count)
        else:
            thread_length = calculate_thread_length(rug_lengths,
                                                    short_rug_thread_count)
        print(f"{length_txt} m vaibale kulub {thread_length} m lõime")
        total_thread_length += thread_length
    print(
        f"Kõikide vaipade peale läheb vaja {total_thread_length} meetrit lõimeniiti.")
    # print(calculate_thread_length(7, 120))
