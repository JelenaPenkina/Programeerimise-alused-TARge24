def exercise_eight():
    """
    Küsi kasutajalt arvu ja järgi seda, kuidas arv on:
    - Kui positiivne, palu sisestada negatiivne arv.
    - Kui negatiivne, palu sisestada positiivne arv.
    - Kui 0, õnnitle ja ütle, et olete mängu ära teinud.
    - Kuvage sisestatud arvud kahanevas järjekorras.
    """
    numbers = []

    while True:
        try:
            number = int(input("Sisesta number: "))
        except ValueError:
            print("Palun sisesta korrektne number.")
            continue

        if number > 0:
            print("Proovi pigem negatiivset arvu.")
        elif number < 0:
            print("Proovi pigem positiivset arvu.")
        else:
            print("Õnnitleme, olete mängule ära teinud! Pääsete igavesest kordusest!")
            break

        numbers.append(number)

    # Kuvame numbrid kahanevas järjekorras
    numbers.sort(reverse=True)
    print("Sisestatud arvud kahanevas järjekorras:", numbers)


if __name__ == "__main__":
    exercise_eight()

#
# def exercise_eight2():
#     """
#     Küsi kasutajalt arvu ja järgi seda, kuidas arv on:
#     - Kui positiivne, palu sisestada negatiivne arv.
#     - Kui negatiivne, palu sisestada positiivne arv.
#     - Kui 0, õnnitle ja ütle, et olete mängu ära teinud.
#     - Kuvage sisestatud arvud kahanevas järjekorras.
#     """
#     numbers = []
#
#     # Küsimiseks kasutame for tsüklit. Üks kord küsime sisendi.
#     for _ in range(1):
#         try:
#             number = int(input("Sisesta number: "))
#             break  # Kui number on sisestatud õigesti, siis katkestame tsükli.
#         except ValueError:
#             print("Palun sisesta korrektne number.")
#
#     if number > 0:
#         print("Proovi pigem negatiivset arvu.")
#     elif number < 0:
#         print("Proovi pigem positiivset arvu.")
#     else:
#         print("Õnnitleme, olete mängule ära teinud! Pääsete igavesest kordusest!")
#
#     numbers.append(number)
#
#     # Kuvame numbrid kahanevas järjekorras
#     numbers.sort(reverse=True)
#     print("Sisestatud arvud kahanevas järjekorras:", numbers)
#
# if __name__ == "__main__":
#     exercise_eight2()