import random
from operator import mul, sub, add
from tokenize import endpats


def solution():
    name = input("Palun siseta oma nimi? ")
    for i in range(5):
        print(f'Ole tervitatud, {name}, {i + 1}. korda.')


def sum_unlimited():
    """
    Summeri kõik sisestatud arvud kuni sisestud ei ole arv.
    """
    total = 0
    counter = 1
    while True:
        number = input(f'Siseta arv #{counter}: ')
        if not number.isnumeric():
            break
        number = int(number)
        total += number
        counter += 1
    print(f'Kõik kokku on: {total}')


def sum_ten_for():
    total = 0
    for i in range(10):
        number = int(input(f'Siseta arv #{i + 1}: '))
        total += number
    print(f'Kokku on: {total}')


def sum_ten_while():
    counter = 0
    total = 0
    while counter < 10:
        number = int(input(f'Siseta arv #{counter + 1}: '))
        counter += 1
        total += number
    print(f'Kokku on: {total}')


def calculator():
    user_counter = int(input('Mitu tehte soovid teha? '))
    min_num = int(input('Mis on miinimum number: '))
    max_num = int(input('Mis on maksimum number: '))
    print(
        f'Tere! Õpime arvutama. Esitan {user_counter} arvutustehet, püüa vastata õigesti.')
    operators = {"+": add, "-": sub, "*": mul}
    keys = list(operators)
    counter = 0
    correct_answer = 0
    while counter < user_counter:
        number1 = random.randint(min_num, max_num)
        number2 = random.randint(min_num, max_num)
        my_operator = random.choice(keys)
        input_answer = int(
            input("{} {} {} = ".format(number1, my_operator, number2)))
        if input_answer != (operators[my_operator](number1, number2)):
            print(
                f'Sinu vastus polnud õige. Õige vastus on {operators[my_operator](number1, number2)}. ')
        else:
            print(f'Tubli, õige vastus!')
            correct_answer += 1
        counter += 1
    print(
        f'See oli viimane ülesanne. Kogusid {user_counter}-st punktist {correct_answer}.')

    result = correct_answer / user_counter * 100
    give_result(result)


def give_result(result):
    if result > 90:
        print('Ülihea')
    elif result > 70:
        print('Olid tubli')
    elif result >= 50:
        print('Korralik keskmine tulemus!')
    else:
        print('Püüad järgmisel korral rohkem.')


def lesson_six():
    counter = 0
    for i in range(20):
        for j in range(20):
            for k in range(20):
                print(f'{i + 1} - {j + 1} - {k + 1}')
                counter += 1
    print(f'Kokku on: {counter}')


def lesson_seven():
    """
    Koosta programm, mis küsib kasutajalt arvu N ja väljastab O-tähtedest
    koosneva ruudu suuruses NxN. Seejärel muutke programmi nii, et ruudu
    diagonaalidel olevad märgid oleksid X-d, näiteks:
    """
    user_input = int(input('Mitu rida soovid teha '))
    for row in range(user_input):
        for col in range(user_input):
            symbol = 'O'
            if row == col:
                symbol = 'X'
            if col + row == (user_input - 1):
                symbol = 'X'
            print(f'{symbol}', end=' ')
        print()


if __name__ == '__main__':
    lesson_seven()
