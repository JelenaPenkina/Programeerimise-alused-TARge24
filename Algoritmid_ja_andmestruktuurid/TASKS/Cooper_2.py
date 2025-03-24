"""
Funktsioon, mis võtab argumentideks meetrite arvu ja jooksja soo ning tagastab:

•	Sõne „väga hea“, kui meetreid on meeste puhul vähemalt 2800 ja naiste puhul 2600 vähem
•	Sõne „nõrk“, kui meetreid on meeste puhul vähem kui 2000 ja naistel alla 1800
•	Sõne „rahuldav“ muudel juhtudel
•	Tulemused, mis jäävad alla „väga hea“, peavad lisaks teatama, mitu meetrit jäi järgmisest hindest puudu

"""

with open('cooper_vol2.txt', 'w', encoding='utf8') as f:
    f.write("""1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N
""")


def read_file(file_name) -> list:
    """

    :param file_name:
    :return:
    """
    result = []
    with open(file_name, "r", encoding='utf8') as file:
        for line in file:
            result.append(line.rstrip())
    return result


def get_cooper_result(distance: int, is_male: bool) -> tuple[str, None]:
    """
    Return cooper test result "Väga hea", "nõrk", "rahuldav"
    :param distance: distance in meters ran in 12 minutes
    :param is_male: participant is male or not
    :return: tupl where first value is rseult and second distance remaingi to g
    """
    result = "väga hea"
    distance_to_next = None
    if distance < 2000 and is_male or distance < 1800 and not is_male:
        result = "nõrk"
        distance_to_next = 2000 - distance if is_male else 1800 - distance
    elif distance < 2800 and is_male or distance < 2600 and not is_male:
        result = "rahuldav"
        distance_to_next = 2800 - distance if is_male else 2600 - distance
    return result, distance_to_next


def process_results(results_from_file: list[str]):
    """
    Split each element first value is integer distance, second gender "M" for male,
    "N" for female
    :param results_from_file:
    :return: tuple(list of each element's cooper result, average results for both genders)
    """
    results = []
    male_distance_count = 0
    male_distance_sum = 0
    female_distance_count = 0
    female_distance_sum = 0
    for line in results_from_file:
        distance_txt, gender_txt = tuple(line.split())
        distance = int(distance_txt)
        if gender_txt == "M":
            male_distance_sum += distance
            male_distance_count += 1
            cooper_result = get_cooper_result(distance, True) + (
                gender_txt, distance_txt)
        else:
            female_distance_sum += distance
            female_distance_count += 1
            cooper_result = get_cooper_result(distance, False) + (
                gender_txt, distance_txt)
        results.append(cooper_result)
    average_distance = round(male_distance_sum / male_distance_count)
    male_average_result = get_cooper_result(average_distance, True) + (
        "M", str(average_distance))
    average_distance = round(female_distance_sum / female_distance_count)
    female_average_result = get_cooper_result(average_distance, False) + (
        "N", average_distance)
    return results, [male_average_result, female_average_result]


def display_cooper_results(cooper_results):
    """

    :param cooper_results:
    """
    for result, distance_to_next, gender, distance in cooper_results:
        if distance_to_next:
            print(
                f'{gender} {distance} m, {result}, järgmisest hindest puudu {distance_to_next}')
        else:
            print(f'{gender} {distance} m, {result}')


if __name__ == '__main__':
    filename = input("Sisesta cooper testi tulemuste faili nimi: ")
    results_from_file = read_file(filename)
    cooper_results, average_results = process_results(results_from_file)
    display_cooper_results(cooper_results)
    print('Keskmised:')
    display_cooper_results(average_results)