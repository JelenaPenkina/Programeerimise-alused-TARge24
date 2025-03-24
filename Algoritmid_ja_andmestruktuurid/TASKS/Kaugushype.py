"""
•	lugema failist vigased tulemused (meetrites);
•	funktsiooniga arvutama tegelikud tulemused ja väljastama need ekraanile (ümardatuna kahe kümnendkohani pärast koma);
•	arvutama ja väljastama ekraanile normatiivi täitnud tegelike tulemuste arvu ja nende keskmise (ümardatuna kahe kümnendkohani pärast koma).
o	Kui normatiivi täitjaid ei ole, siis keskmist ei arvutata ega väljastata.

"""
from cooper.cooper_vol2 import read_file

DEFAULT_FILE_NAME = 'kaugus.txt'

with open(DEFAULT_FILE_NAME, 'w', encoding='utf8') as f:
    f.write("""6.56
5.76
5.82
5.23
5.74
6.14
5.28
5.77
6.45
6.02
5.78
""")


def calculte_new_result(result_to_fix: float, fix_cm: float):
    """
    Calculate new results
    :param result_to_fix: old result to fix
    :param fix_cm: cm to fix old results
    :return:
    """
    return (result_to_fix * 100 + fix_cm) / 100


def print_new_results():
    """
    Print new results.
    """
    results_to_fix = read_file(filename if filename else DEFAULT_FILE_NAME)
    norm_count = 0
    average_sum = 0
    print('Tegelikud tulemused')
    for result in results_to_fix:
        result = float(result)
        result = calculte_new_result(result, float(result_fix))
        if result > float(qualify_norm):
            norm_count += 1
            average_sum += result

        print(result)
    print(f'Normatiivi täitis {norm_count}.')
    print(f'Täitnute keskmine on {average_sum / norm_count:.2f}.')


if __name__ == '__main__':
    filename = input(f'Sisesta failinimi [{DEFAULT_FILE_NAME}]: ')
    result_fix = input('Sisestage parandus sentimeetrites: ')
    qualify_norm = input('Sisestage meistrivõistluste normatiiv meetrites: ')

    print_new_results()