import random
"""
7 ülesanne 
    1. Küsi kasutajalt 1 arv mille paned astmele 2,3,4 ja 5 kasutades kordust ja järjend
    2. Lase kasutajal arvata, millises astmes on suvaline arv järjendis 
    3. Teata kas arvati õigesti ja kuva õige vastus  
    4. Peale seda küsi kastutajalt kas ta soovib teise arvuga programmi korrata või lõpetada (kordus)
"""

def power_guess_game():
    while True:
        try:
            num = int(input("Sisesta üks arv: "))
        except ValueError:
            print("Palun sisesta ainult numbreid!")
            continue

        powers = [num ** i for i in range(2, 6)]
        random_value = random.choice(powers)
        print("Üks järjendis olevatest väärtustest on:", random_value)

        try:
            guess = int(input("Millises astmes see arv oli? (2-5): "))
        except ValueError:
            print("Palun sisesta korrektne number!")
            continue

        correct_power = powers.index(random_value) + 2

        if guess == correct_power:
            print("Õige vastus!")
        else:
            print(f"Vale! Õige vastus oli {correct_power}.")

        repeat = input("Kas soovid uuesti proovida? (jah/ei): ").strip().lower()
        if repeat != "jah":
            print("Aitäh mängimast!")
            break


if __name__ == "__main__":
    power_guess_game()