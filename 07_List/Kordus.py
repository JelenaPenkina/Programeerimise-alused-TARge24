# Algväärtus vealoendurile
vead = 0
ootame_paaris = True  # Alguses peab kasutaja sisestama paaris arvu

while vead < 5:
    arv = input("Sisesta " + ("paaris" if ootame_paaris else "paaritu") + " arv: ")

    if not arv.isdigit():
        print("Palun sisesta täisarv!")
        vead += 1
        continue

    arv = int(arv)

    # Kontrollime, kas arv vastab oodatule
    if (ootame_paaris and arv % 2 == 0) or (not ootame_paaris and arv % 2 != 0):
        print("Õige!")
        ootame_paaris = not ootame_paaris  # Vaheta järgmist sisendit
    else:
        print("Vale! See ei ole " + ("paaris" if ootame_paaris else "paaritu") + " arv.")
        vead += 1

print("Eksisid 5 korda, programm lõppeb.")
