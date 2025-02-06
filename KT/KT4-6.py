#4
gender = input("Sisesta oma sugu (M/N): ").upper()
age = int(input("Sisesta oma vanus: "))

if gender == "M":
    greeting = "Tere, härrasmees!"
else:
    greeting = "Tere, proua!"

# Korda tervitust vastavalt eale kuni 10 korda
for i in range(min(10, age)):
    print(f"{greeting} Vanus: {age + i}")


#5
name = input("Sisesta oma nimi: ")

if 5 <= len(name) <= 10:
    for _ in range(3):
        print(f"Tere, {name}!")
else:
    nums = [int(input(f"Sisesta {i+1}. arv: ")) for i in range(3)]
    print(f"Nende arvude summa on: {sum(nums)}")

#6
word = input("Sisesta sõna: ")
number = int(input("Sisesta number: "))

if number > 10:
    print("Viga")
else:
    for _ in range(number * 2):
        print(word)

#7
while True:
    num = int(input("Sisesta üks arv: "))

    for power in range(2, 6):
        print(f"{num} ** {power} = {num ** power}")

    choice = input("Kas soovid sisestada teise arvu? (jah/ei): ").lower()
    if choice != "jah":
        break

#8
while True:
    num = int(input("Sisesta arv: "))

    if num > 0:
        print("Proovi pigem negatiivset arvu!")
    elif num < 0:
        print("Proovi pigem positiivset arvu!")
    else:
        print("Õnnitlen, mäng on lõppenud!")
        break

