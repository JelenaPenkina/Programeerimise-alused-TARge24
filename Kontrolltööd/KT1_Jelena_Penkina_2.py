"""
Ül 2.

    Küsi kasutaja nime ja vanust
    Kui vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
    Muidu küsi koosta nime pikkuse jagu arvutus tehteid juhuarvudega (Järjend)
    Kuva tehteid ja lase kasutajal vastata, teata kas said õige tulemuse.
    Programmi lõpus õnnitle kasutajat erineva tekstiga olenevalt programmi käigust

"""


def user_name():
    """
    Küsi kasutajalt nime ja vanust.
    If age lower or equals than 5 years old then say "Tere, {name}!" three times

    :param: Prindib kasutaja nime ja vanust.
    :type: str and int
    :param: kui vanus on <=5, prindib kolm korda "Tere {name}"
    :type: str
    :return: user name and age
    """
    name = input("Kasutaja nimi: ")  # küsib kasutaja nime
    age = int(input("Kasutaja vanus: "))
    if age <= 5:
        for i in range(3):
            print(f"Tere {name}")
    else:
        return name, age


def list_number():
    """
    Tehete kuvamine ning kui kasutaja kirjutab õige vastuse kuvatakse "Õige", kui vale siis
    Vale! Vastus on "

    :param: random numbrid ning kasutaja arvutustehte arvutamine
    :type: int
    :param: Kui vale vastus, annab õige vastuse tagasi
    :type: int
    :return: Lõpus õnnitleb kasutajat mängu lõpetamisega
    :type: str
    """
    from random import randint
    num_a = randint(1, 20)
    num_b = randint(1, 20)
    total = sum
    result = input(f"{num_a} + {num_b} = ")
    if result is True:
        print(f"Õige! {total}")
    elif result is False:
        print(f"Vale! Vastus on {result}")
    else:
        return print("Palju õnne mäng on läbi! ")


if __name__ == '__main__':
    print(user_name())
    print(list_number())
