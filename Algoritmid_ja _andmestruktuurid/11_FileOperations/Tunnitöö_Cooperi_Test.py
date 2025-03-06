"""
Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga.
On määratud erinevad hindenormid meestele ja naistele.

Koostada programm, mis küsib kasutajalt:
•	failinime,
Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni
    ümardatud keskmised ning funktsiooni abil keskmised hinded.
"""
from unittest import result

""" # with open("cooper.txt", encoding="utf8") as file:
    print(file.read())

def cooper_test(soo, kaugus):
    if soo == "N":
        if kaugus >= 2600:
            return "Väga hea"
        elif kaugus >= 1800:
            return "Nõrk"
        else:
            return "Rahuldav"
    if soo == "M":
        if kaugus >= 2800:
            return "Väga hea"
        elif kaugus >= 2000:
            return "Nõrk"
        else:
            return "Rahuldav" """

# Õpetaja versioon

with open("cooper.txt", "w", encoding="utf8") as file:
    file.write("""1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N """)


def get_cooper_result(distance: int, is_male: bool) -> tuple[str, None]:
    """
    Return cooper test result "rahuldav", "väga hea", "nõrk" and distance to next up
    :param distance: distance in meters ran in 12 minutes
    :param is_male: participant is male or not?
    :return: tuple where is the result and second distance remaining to get 
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


file_name = "cooper.txt"


def read_file(file_name) -> list:
    results = []
    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            result.append(line.strip())
    return result


def process_results(results_from_file: list[str]):
    """
    Split each element first value is integer distance, second gender "M" - for male and "N" - for female
    :param result_from_file:
    :return: tuple(list of each element's cooper result , average result for both genders)
    """
    results = []
    male_distance_count = []
    male_distance_sum = []
    female_distance_count = []
    female_distance_sum = []
    for line in results_from_file:
        distance_txt, gender_txt = tuple(line.split())
        distance = int(distance_txt)
        if gender_txt == "M":
            male_distance_count += distance
            male_distance_count += 1
            cooper_result = get_cooper_result(distance, True) + (
            gender_txt, distance_txt)
        else:
            female_distance_count += distance
            female_distance_count += 1
            cooper_result = get_cooper_result(distance, False) + (
            gender_txt, distance_txt)
        results.append(cooper_result)
    average_distance = round(male_distance_sum / male_distance_count)
    male_average_result = get_cooper_result(
        round(male_distance_sum / male_distance_count), True) + (
                          "M", str(average_distance))
    average_distance = round(female_distance_sum / female_distance_count)
    female_average_result = get_cooper_result(
        round(female_distance_sum / female_distance_count), False) + (
                            "N", str(average_distance))
    return results, [male_average_result, female_average_result]


def display_cooper_results(cooper_results):
    """
    Print results to console
    :param cooper_results:
    :return:
    """
    for result, distance_to_next, gender, distance in cooper_results:
        if distance_to_next:
            print(f"{result}: {distance} ({gender})")


if __name__ == "__main__":
    filename = input("Sisesta cooper teksti tulemuste nimi: ")
    result_from_file = read_file(file_name)
    cooper_results = process_results(result_from_file)
    display_cooper_results(cooper_results[0])
    print("Keskmised")
    display_cooper_results(cooper_results[1])

    # for result, distance_to_next, gender, distance in cooper_results[0]:
    # if distance_to_next:
    #    print(f"{gender} {distance} m, {result}) , järgmisest hindest puudu {distance_to_next} m")
    # else:
    #    print(f"{gender} {distance} m, {result}")

# print(f"{gender} {distance} m, {result} {', järgmisest hindest puudu ' + str(distance_to_next) + ' m' if distance_to_next else ''}")
