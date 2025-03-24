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