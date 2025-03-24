"""
Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja
eesnimed (iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult).
Koosta programm, mis loeb failist andmed ja väljastab need ekraanile
tähestikulises järjekorras. Mõistlik on ilmselt kasutada järjendit ja sellega
seonduvaid võimalusi (järjestamist). Tähestikulises järjekorras salvestage
tuttavate nimed ka uude faili tuttavad1.txt.
"""


def create_file(file_name: str, lines: list) -> None:
    with open(file_name, "w") as file:
        for line in lines:
            file.write(f'{line}\n')


def read_file(file_name) -> list:
    result = []
    with open(file_name, "r") as file:
        for line in file:
            result.append(line.strip())
    return result

    # return file.read().splitlines()


def split_words(sentences: list) -> list:
    result = []
    for sentence in sentences:
        result.append(tuple(sentence.split()))
    return result


if __name__ == '__main__':
    file_name = 'tuttavad.txt'
    create_file(file_name, ['Tiit Sull', 'Ott Sepp', 'Elina Lill',
                            'Joosepe Juurikas', 'Peep Vain', 'Jaan Järv'])
    names = read_file(file_name)
    split_names = split_words(names)
    print(split_names)
    sorted_names = list(
        map(lambda s: " ".join(s), sorted(split_names, key=lambda n: n[-1])))
    for name in sorted_names:
        print(f'{name}')
    create_file('sorteeritud_tutavad.txt', sorted_names)