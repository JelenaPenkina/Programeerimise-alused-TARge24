from operator import length_hint

user_age = int(input("Enter your age: "))
user_name = input("Enter your name: ")

for i in range(user_age - 1):
    print(f"Tere {user_name}!")
print(user_name[len(user_name) - 3:])


def exercise_three():
    """
    1.1 Küsi kasutajalt nime ja vanust.
    1.2 Õnnitle kasutajat iga täisealisena veedetud aasta eest.
    1.3 Iga õnnitluse järel küsi ja salvesta meeleolu.
    1.4 Kuvab programmi lõpus meeleolud pikkuse järjekorras.
    """
    # 1.1 Küsi kasutajalt nimi ja vanus
    name = input("Sisesta oma nimi: ")
    while True:
        try:
            age = int(input("Sisesta oma vanus: "))
            break
        except ValueError:
            print("Palun sisesta ainult numbrid!")

    # Kontrolli, kas kasutaja on täisealine
    if age < 18:
        print("Sa ei ole veel täisealine, tule tagasi hiljem! ")
        return

    # 1.2 Õnnitle iga täisealisena veedetud aasta eest
    meeleolud = []
    print(f"\nPalju õnne, {name}! Oled olnud täisealine juba {age - 18} aastat! ")

    for i in range(age - 18):
        print(f"Palju õnne täisealisuse aasta {i + 1} puhul! ")

        # 1.3 Küsi ja salvesta meeleolu
        meeleolu = input(f"Kuidas tundsid end {18 + i}-aastasena? ")
        meeleolud.append(meeleolu)

    # 1.4 Kuvab meeleolud pikkuse järjekorras
    meeleolud.sort(key=len)
    print("\nSiin on sinu meeleolud järjestatud pikkuse järgi:")
    for mood in meeleolud:
        print(mood)


if __name__ == "__main__":
    exercise_three()