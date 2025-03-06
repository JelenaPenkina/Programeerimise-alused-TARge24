# Loo nimekiri tuttavate nimedega
names = ["Mati", "Kati", "Jüri"]

# Küsi kasutajalt, kas ta tunneb neid
for i in range(len(names)):
    response = input(f"Kas sa tunned {names[i]}? (jah/ei): ").lower()
    if response == "ei":
        names[i] = input("Sisesta uus nimi: ")

# Väljasta lõplik nimekiri
for name in names:
    print(name)
