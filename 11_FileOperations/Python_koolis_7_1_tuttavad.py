"""Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale,
perekonna- ja eesnimi tühikuga eraldatult). Koosta programm, mis loeb failist andmed ja väljastab need
ekraanile tähestikulises järjekorras. Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi
 (järjestamist). Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili sorteeritud_tuttavad1.txt """


# file_name = "sorteeritud_tuttavad1.txt"

def create_file(file_name: str, lines: list) -> None:
    """ Write each value in lines to separate line in file."""
    # file_name = "sorteeritud_tuttavad1.txt"
    # with open(file_name, "w", encoding="utf-8") as file:
    # with open(file_name, "a") as file:
    # for line in lines:
    # file.write(line + "\n")
    # Õpetaja versioon


with open(file_name, "a") as file:
    for line in lines:
        file.write(line)
        file.write("\n")


def read_file(file_name) -> list:
    """ Read all line to a list and return that list """
    result = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in sorted_names:
            result.append(line)
    return result


def split_words(sentences: list) -> list:
    """
    Split sentences into tuple of words and return them

     sentences:["See on sisend lause", "Siin on ka lause", "veel"]
     :return: (["See", "on" "sisend", "lause", ("Siin", "on", "ka", "lause", "veel"])
     """
    result = []
    for sentence in sentences:
        result.append(tuple(sentence.split()))


if __name__ == '__main__':
    file_name = "tuttavad.txt"
    create_file(file_name,
                ["Tiit Sukk", "Armas Nool", "Elina Elli", "Joosep Juuri",
                 "Tauno Kuusik", "Mark Tippi"])
    names = read_file(file_name)
    print(names)
    split_names = split_words(names)
    print(split_names)
    sorted_names = sorted(names, key=lambda n: n[-1])
    for name in sorted_names:
        print(f"{' '.join(name)}")
    # TODO Display each name on a separate line
    create_file("sorteeritud_tuttavad.txt", sorted_names)
