# HarjutamineKontrolltööks 1: Kolme arvu küsimine ja kontrollimine kasutajalt

def main():
    # 1. Küsi kasutajalt 3 arvu ja salvesta need loendisse
    arvud = [int(input(f'Sisestage {i + 1}. arv: ')) for i in range(3)]

    # 2. Leia väikseim arv ja korruta see kahega
    vaikseim_arv = min(arvud) * 2
    print(f'Väikseim arv korrutatuna kahega: {vaikseim_arv}')

    # 3. Küsi kasutajalt iga arvu ruutu 1 kuni vaikseim_arv (kasutades kordust)
    oiged_vastused = 0
    for i in range(1, vaikseim_arv + 1):
        vastus = int(input(f'Mis on {i} ruut? '))
        if vastus == i ** 2:
            print('Õige!')
            oiged_vastused += 1
        else:
            print(f'Vale! Õige vastus on {i ** 2}')

    # 4. Teata, mitu korda kasutaja vastas õigesti
    print(f'Kokku vastasid õigesti {oiged_vastused} korda.')


# Küsi kasutaja nime ja vanust HarjutamineKontrolltööks-2
name = input("Sisesta oma nimi: ")
age = int(input("Sisesta oma vanus: "))

if len(name) < age or age < 5:
    for _ in range(3):
        print(f"Tere, {name}!")
else:
    nums = [int(input(f"Sisesta {i + 1}. arv: ")) for i in range(3)]
    total = sum(nums)
    user_sum = int(input("Sisesta arvude summa: "))

    if user_sum == total:
        print("Õige!")
    else:
        print("Vale!")


"""# Küsi kasutaja nime ja vanust
name = input("Sisesta oma nimi: ")
age = int(input("Sisesta oma vanus: "))

# Arvuta täisealisuse aastad (18-aastane on täisealine)
adult_years = max(0, age - 18)

# Tervita vastavalt täisealisuse aastatele
for _ in range(adult_years):
    print(f"Tere, {name}!")

# Väljasta viimased 3 tähte nimest
print(f"Sinu nime viimased 3 tähte: {name[-3:]}") """


# Käivitab programmi
if __name__ == "__main__":
    main()