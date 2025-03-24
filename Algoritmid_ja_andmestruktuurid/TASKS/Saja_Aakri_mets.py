"""
•	küsib kasutajalt
    o	failinime (failis on eraldi ridadel metsatükkide pindalad aakrites);
    o	vastava puuliigi aastase juurdekasvu hektari kohta tihumeetrites (ujukomaarv);
    o	piiri, mitmest aakrist suuremad metsatükid arvesse võtta (ujukomaarv);
•	loeb failist metsatükkide pindalad;
•	arvutab (funktsiooni abil) ja väljastab metsatüki aastase juurdekasvu, kui selle metsatüki pindala on sisestatud piirist suurem;
•	väljastab teate “Metsatükki ei võeta arvesse”, kui metsatüki pindala ei ole sisestatud piirist suurem;
•	väljastab lõpuks ekraanile, mitme metsatüki juurdekasv arvutati.

"""
from cooper.cooper_vol2 import read_file

DEFAULT_FILE_NAME = 'andmed.txt'

with open(DEFAULT_FILE_NAME, 'w', encoding='utf8') as f:
    f.write("""0.9
3.78
2.05
1.58
""")


def calculate_year_growth(area: float, year_growth_rate: float) -> float:
    """

    :param area:
    :param year_growth_rate:
    :return:
    """
    return round(year_growth_rate * area * 0.4047, 2)


def print_growth(growth_rate: float, marginal: float) -> None:
    areas_from_file = read_file(filename if filename else DEFAULT_FILE_NAME)
    over_marginal_count = 0
    for area in areas_from_file:
        area_float = float(area)
        if area_float < marginal:
            print('Metsatükki ei võeta arvesse')
        else:
            over_marginal_count += 1
            print(
                f'Metsatüki aastane juurdekasv on {calculate_year_growth(area_float, growth_rate)}')
    print(f'Arvutati {over_marginal_count} metsatüki juurekasv')


if __name__ == '__main__':
    filename = input(f'Sisesta failinimi [{DEFAULT_FILE_NAME}]: ')
    jewish_growth = float(
        input('Sisestage aastane juurdekav hektari kohta tihumeetrites: '))
    marginal_rate = float(input(
        'Sisestage piir, mitmest aakrist suuremad metsatükid arvesse võtta: '))
    print_growth(jewish_growth, marginal_rate)