# Küsi kasutajalt sugu ja vanus
gender = input("Sisesta sugu (M/N): ").strip().upper()
user_age = int(input("Sisesta vanus: "))

# Tervitused soo ja vanuse põhjal
if gender == 'M':
    greetings = "Tere, härra!"
elif gender == 'N':
    greetings = "Tere, proua!"
else:
    print("Sisestasid vale soo. Proovi uuesti.")
    exit()

# Alustame tervituse kordamisega
for i in range(10 or user_age >= 61):
    print(f"{greetings} Teie vanus on nüüd {user_age}.")

    # Kontrolli, kas tervitus muutub
    user_age += 1
    if gender == 'M' and user_age >= 60:
        greetings = "Tere, auväärne härrasmees!"
    elif gender == 'N' and user_age >= 60:
        greetings = "Tere, auväärne daam!"



def exercise_four():
    """
    1.1 Küsi kasutajalt sugu ja vanus.
    1.2 Kasuta vanusele vastavaid tervitusi nii mehele kui naisele.
    1.3 Korda tervitust vanuse suurendamisega kuni tervitus vahetub või 10 korda.
    1.4 Salvesta järjendisse iga kolmas tervitus ja viimane.
    1.5 Kuva ekraanile järjendis olevate tervituste eelviimased sõnad.
    """
    # 1.1 Küsi kasutajalt sugu ja vanus
    sugu = input("Sisesta oma sugu (mees/naine): ").strip().lower()
    while sugu not in ["mees", "naine"]:
        print("Palun sisesta kas 'mees' või 'naine'!")
        sugu = input("Sisesta oma sugu (mees/naine): ").strip().lower()

    while True:
        try:
            vanus = int(input("Sisesta oma vanus: "))
            break
        except ValueError:
            print("Palun sisesta kehtiv arv!")

    # 1.2 Tervitused vanuse põhjal
    if sugu == "mees":
        tervitused = ["Tere, noormees!", "Tere, härrasmees!", "Tere, auväärne mees!"]
    else:
        tervitused = ["Tere, noor daam!", "Tere, proua!", "Tere, auväärne naine!"]

    salvestatud_tervitused = []
    eelmine_tervitus = None

    for i in range(10):
        # Vanus suureneb igal tsükli korral
        vanus += 1
        # Valime vanuse järgi sobiva tervituse
        if vanus < 25:
            tervitus = tervitused[0]
        elif vanus < 50:
            tervitus = tervitused[1]
        else:
            tervitus = tervitused[2]

        print(tervitus)

        # Kui tervitus muutub, katkestame tsükli
        if eelmine_tervitus and eelmine_tervitus != tervitus:
            break

        # 1.4 Salvesta iga kolmas tervitus ja viimane
        if (i + 1) % 3 == 0 or i == 9:
            salvestatud_tervitused.append(tervitus)

        eelmine_tervitus = tervitus

    # 1.5 Kuva ekraanile järjendis olevate tervituste eelviimased sõnad
    print("\nSalvestatud tervituste eelviimased sõnad:")
    for tervitus in salvestatud_tervitused:
        words = tervitus.split()
        if len(words) > 1:
            print(words[-2])


if __name__ == "__main__":
    exercise_four()