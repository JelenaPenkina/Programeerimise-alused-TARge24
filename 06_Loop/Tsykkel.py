"""
Koosta programm, mis küsib kasutajalt nime ja tervitab teda nimeliselt 5 korda ja lisab ka tervituse järjekorranumber.
Palun sisesta oma nimi:
>> Siim
Ole tervitatud, Siim, 1. korda.
Ole tervitatud, Siim, 2. korda.
Ole tervitatud, Siim, 3. korda.
Ole tervitatud, Siim, 4. korda.
Ole tervitatud, Siim, 5. korda.
"""


# Ülesanne 1
def name(name: str, nr: int) -> str:
    for name in range(5):
        print(f"Ole tervitatud, {name},")
# Õpetaja variant

def solution():
    name = input("Palun sisest oma nimi: ")
    for i in range(5):
        print(f"Ole tervitatud, {name}, {i + 1}. korda.")
# 2 Ülesanne
""" 
Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa. 
Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga. 
"""
# for
def sumOfNumbers():
    nr = input("Kirjuta 10 arvu: ")
    for i in sum():
        return sum(i + nr)


def numbersList():
    count = 0
    nr = input("Kirjuta arvud: ")
    while True:
        print(nr)
        return count
        break

# Õpetaja varaint
# def sum_ten_for():

def sum_ten_while():
    counter = 0
    total = 0
    while counter < 10:
        counter += 1
        user_number = int(input(f"Sisesta {counter}. Täisarv: "))
        total += user_number
    print(f"Sisestatud arvude summa on {total}")


def sum_of_unlimited():
    counter = 0
    total = 0
    while True:  # TODO kirjutada õige tingimus
        counter += 1
        user_input = input(
            f"Sisesta {counter}.")  # TODO lahuta küsimine ja arvuks tegemine
        # return int(user_number)
        if user_input == "":
            break  # TODO katkesta tsükkel teatud juhul
        user_number = int(user_input)
        total += user_number
    print(f"Sisestatud {counter - 1} arvu summa on {total}")


# Ülesanne 3
"""Koosta programm, mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige, kiitma kasutajat, 
kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10), samuti võib olla ette antud piirid, kui suuri arve 
kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse. 
Näiteks:
Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.
5 + 16 =
>> 21
Tubli, õige vastus!
18 + 23 =
>> 39
Sinu vastus polnud õige. Õige vastus on 41.
[...]
2 + 5 =
>> 7
Tubli, õige vastus!
See oli viimane ülesanne. Kogusid 10-st punktist 7.

Täiendusi vabal valikul:

    Programm lubab kasutajal alguses sisestada, mitut tehet soovitakse.
    Esitatavate arvude piirid saab kasutaja ette anda (maksimum või nii miinimum kui maksimum).
    Küsitakse mitte ainult liitmistehteid, vaid ka teisi (lahutamine, korrutamine, jagamine).
    Vastavalt lõpptulemusele reageeritakse erinevalt: "Ülihea!", "Olid tubli!", "Korralik keskmine tulemus!", "Püüad järgmisel korral rohkem." vms. """


def sum_Of_Numbers():
    print("Tere! Õpime arvutama. Esitan 10 liitmistehet, püüa vastata õigesti.")
    from random import randint
    num_a = randint(1, 50)
    num_i = randint(1, 50)
    counter = 0
    result = input(f"{num_a} + {num_i} = ")
    if result is True:
        return f"Tubli, õige vastus!, {counter + 1}"
    elif result is False:
        return f"Sinu vastus polnud õige. Õige vastus on {sum}, {counter}"
    else:
        return f"See oli viimane ülesanne. Kogusid 10-st punktist {counter}."


# Õpetaja versioon
""" def practice_adding(lowest, highest, count):
    from random import randint
    correct_answers = 0
    for i in range(count):
        first_number = randint(lowest, highest)
        second_number = randint(lowest, highest)
        random_operator = randint(1,3)
        if random_operator == 1:
def show_equation(operation_symbol, correct_answer, first_number, second_number):
        user_answer = int(input(f"{first_number} + {second_number} = "))
        if user_answer == correct_answers:
            print("Correct! Very smart")
            correct_answers += 1
        else:
            print("Room for improvement!")
            print(f"{first_number} + {second_number} = {correct_answers}")

    print(f"You tried {count} times and got the answer correct {correct_answers} times.") """

# 6 Ülesanne
""" Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 
1-st 20-ni (20 kaasaarvatud). Samuti loenda, mitu sellist kombinatsiooni leiti. Tulemus:  

def combination_of_Numbers(x, y, z):
    from random import randint
    x = randint(1, 20)
    y = randint(1, 20)
    z = randint(1, 20)
    count = 0

    while print(f"{x} - {y} - {z}"):
        if True:
            print(f"{count}")
            count += 1
        else:
            break

    result = input(f"Kui palju kombinatsiooni kokku tuli: {count}")
"""
# ÕPETAJA versioon
""" counter = 0
for z in range(1, 21):
    for y in range(1,21):
        for x in range(1,21):
            print(f"{z} - {y} - {x}")
            counter += 1
print(f"Kokku leiti {counter} kombinatsiooni") """

# 7 ÜLESANNE
"""Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest koosneva ruudu suuruses NxN. 
   Seejärel muutke programmi nii, et ruudu diagonaalidel olevad märgid oleksid X-d, näiteks: """


def print_square(size):
    # number = input("Kirjuta number:")
    for row in range(size):
        for col in range(size):
            symbol = "O"
            if row == col or row + col + 1 == size:
                symbol = "X"
            print(f"{symbol}", end=" ")
        # if row and col == [0, 0]:
        #   print(f"N", end=" ")
        print()



if __name__ == "__main__":
    # solution()
    # resultOfNumbers()
    # numbersList()
    # sum_ten_while()
    # sum_of_unlimited()
    # sum_Of_Numbers()
    # practice_adding(1,1,5)
    # practice_adding(1, 1, 4)
    # lowest = int(input("Sisesta väiksem täisarv, mida kasutada: "))
    # highest = int(input("Sisesta suurem täisarv, mida kasutada: "))
    # count = int(input("sisesta tehete arv: "))
    # practice_adding(lowest, highest, count)
    # combination_of_Numbers(1,5,10)
    size = int(input("Kui suurt ruutu soovid:  "))
    print_square(size)
