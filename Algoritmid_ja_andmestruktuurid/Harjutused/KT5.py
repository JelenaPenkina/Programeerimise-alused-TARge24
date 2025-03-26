def exercise_five():
    """
    1.1 Küsi kasutajalt lause.
    1.2 Kui lauses on vähem kui 5 sõna, korruta see kasvavalt kuni kasutaja antud numbrini (kordus, järjend).
    1.3 Kui lauses on 5 või rohkem sõna, kuva iga sõna eraldi real.
    """
    # 1.1 Küsi kasutajalt lause
    lause = input("Sisesta üks lause: ").strip()

    # Jaga lause sõnadeks
    sonad = lause.split()

    # 1.2 Kui lauses on vähem kui 5 sõna, küsi arv ja korruta lause
    if len(sonad) < 5:
        while True:
            try:
                kordade_arv = int(input("Sisesta üks arv: "))
                break
            except ValueError:
                print("Palun sisesta kehtiv number!")

        if kordade_arv > 10:
            print("Viga")
        else:
            tulemus = [lause * (i + 1) for i in range(kordade_arv)]
            print("\nViimane korrutatud lause:")
            print(tulemus[-1])

    # 1.3 Kui lauses on 5 või rohkem sõna, kuva iga sõna eraldi real
    else:
        print("\nSõnad eraldi reas:")
        for sona in sonad:
            print(sona)


if __name__ == "__main__":
    exercise_five()