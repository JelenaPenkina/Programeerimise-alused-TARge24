"""
1.       Küsi kasutaja nime ja vanust
2.       Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.       Muidu küsi kolm arvu ja nende summa
4.       Teata kas said õige tulemuse.
"""

name = input("Sisesta oma nimi: ")
age = int(input("Sisesta oma vanus: "))
if len(name) < age or age > 5:
    for i in range(3):
        print("Tere", name + "!")
else:
    number1 = int(input("Sisesta esimene arv: "))
    number2 = int(input("Sisesta teine arv: "))
    number3 = int(input("Sisesta kolmas arv: "))
    sum_answer = int(input(
        "Siseta arvude " + str(number1) + " " + str(number2) + " " + str(
            number3) + " " + " summa: "))
    if sum_answer == (number1 + number2 + number3):
        print("Õige vastus")
    else:
        print("Vale vastus")

import random


def exercise_two():
    """
    1.1 Küsi kasutajalt nime ja vanust.
    1.2 Kui vanus on alla 18, tervita nimepidi 3 korda.
    1.3 Kui vanus on 18 või suurem, loo nime pikkuse jagu juhuarvude tehteid.
    1.4 Küsi kasutajalt iga tehte vastust ja kontrolli, kas see on õige.
    1.5 Programmi lõpus õnnitle kasutajat sõltuvalt tema tulemusest.
    """
    # 1.1 Küsi nimi ja vanus
    name = input("Sisesta oma nimi: ")
    while True:
        try:
            age = int(input("Sisesta oma vanus: "))
            break
        except ValueError:
            print("Palun sisesta ainult numbrid!")

    # 1.2 Kui vanus on alla 5, tervita 3 korda
    if age < 5:
        for _ in range(3):
            print(f"Tere, {name}!")
        print("Sul on veel aega õppida, naudi noorust!")

    else:
        # 1.3 Loo nime pikkuse jagu juhuarvude tehteid
        num_operations = len(name)
        wrong_answers = []

        print(f"\n{num_operations} arvutustehet sulle, {name}!")

        for _ in range(num_operations):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = random.choice(["+", "-", "*"])
            correct_answer = eval(f"{num1} {operator} {num2}")

            while True:
                try:
                    user_answer = int(input(f"Mitu on {num1} {operator} {num2}? "))
                    break
                except ValueError:
                    print("Palun sisesta ainult numbrid!")

            if user_answer == correct_answer:
                print("Õige vastus!")
            else:
                print(f"Vale! Õige vastus oli {correct_answer}.")
                wrong_answers.append((num1, operator, num2, correct_answer))

        # 1.5 Õnnitlus sõltuvalt tulemusest
        if not wrong_answers:
            print("\nSuper töö, kõik vastused olid õiged! ")
        elif len(wrong_answers) <= num_operations // 2:
            print("\nTubli! Enamik vastuseid olid õiged! ")
        else:
            print("\nJärgmine kord läheb paremini, harjutamine teeb meistriks!")


if __name__ == "__main__":
    exercise_two()