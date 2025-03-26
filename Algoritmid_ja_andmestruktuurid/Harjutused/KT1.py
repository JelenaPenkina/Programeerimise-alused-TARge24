"""
 Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda kasutaja vastas õigesti.
"""

import math

"""Ask for input"""
number1 = int(input("Siseta üks arv:"))
number2 = int(input("Siseta teine arv:"))
number3 = int(input("Sisesta kolmas arv:"))

"""Will add all numbers to array"""
numbers = [number1, number2, number3]
numbers.sort()
numbers = [number1 * 2, number2, number3]
print(numbers)

request_until = 1
while request_until < numbers[0]:
    input_result = int(input("Sisesta arv " + str(request_until) + " ruudus: "))
    if input_result == int(math.pow(request_until, 2)):
        print(math.pow(request_until, 2))
        print("Õige vastus")
        request_until += 1
    else:
        print("Vale vastus")


def exercise_one():
    """
    1.1 Küsi kasutajalt 3 arvu.
    1.2 Leia väikseim arv ja korruta see kahega.
    1.3 Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni.
    1.4 Teata, kas kasutaja vastas õigesti või valesti.
    1.5 Näita programmi lõpus kasutaja valesti vastatud ruutude õigeid tulemusi.
    """
    # 1.1 Küsi 3 arvu kasutajalt
    numbers = []
    for i in range(3):
        while True:
            try:
                num = int(input(f'Sisesta {i+1}. arv: '))
                numbers.append(num)
                break
            except ValueError:
                print("Palun sisesta ainult numbrid!")

    # 1.2 Leia väikseim arv ja korruta see kahega
    min_value = min(numbers) * 2
    print(f'Väikseim arv kahekordselt: {min_value}')

    # 1.3 Küsi kasutajalt ruutude väärtusi
    wrong_answers = {}
    for i in range(1, min_value + 1):
        correct_answer = i ** 2
        while True:
            try:
                user_answer = int(input(f'Mis on {i} ruut? '))
                break
            except ValueError:
                print("Palun sisesta ainult numbrid!")

        if user_answer == correct_answer:
            print("Õige!")
        else:
            print("Vale!")
            wrong_answers[i] = correct_answer

    # 1.5 Kuvatakse valesti vastatud ruutude õiged vastused
    if wrong_answers:
        print("\nValesti vastatud ruutude õiged vastused:")
        for key, value in wrong_answers.items():
            print(f"{key}² = {value}")
    else:
        print("\nKõik vastused olid õiged! Tubli töö!")

if __name__ == '__main__':
    exercise_one()