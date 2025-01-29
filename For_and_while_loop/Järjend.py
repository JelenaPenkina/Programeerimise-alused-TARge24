# Tühi järjend loomade jaoks
loomad = []

while True:
    uus_looma_nimi = input("Sisesta looma nimi (või 'lõpeta' lõpetamiseks): ").strip().lower()

    if uus_looma_nimi == "lõpeta":
        break  # Lõpeta programm

    if uus_looma_nimi not in loomad:
        loomad.append(uus_looma_nimi)  # Lisa uus loom nimekirja

    viimase_taht = uus_looma_nimi[-1]  # Leia viimase sisestatud looma viimane täht

    # Otsi looma, mis algab selle tähega
    sobiv_loom = None
    for loom in loomad:
        if loom[0] == viimase_taht:
            sobiv_loom = loom
            break

    if sobiv_loom:
        print(f"Nimekirjas on juba loom, mis algab '{viimase_taht}' tähega: {sobiv_loom}")
    else:
        uus_looma_nimi = input(f"Ühtegi looma pole, mis algaks '{viimase_taht}'. Sisesta uus: ").strip().lower()
        if uus_looma_nimi not in loomad:
            loomad.append(uus_looma_nimi)  # Lisa uus loom nimekirja

# Kuvame lõpliku loomade nimekirja
print("\nLõplik loomade nimekiri:")
for loom in loomad:
    print(loom)
