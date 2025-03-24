"""
1.       Küsi kasutaja nime ja vanust
2.       Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
3.       Muidu küsi kolm arvu ja nende summa
4.       Teata kas said õige tulemuse.
"""

name = input("Sisesta oma nimi: ")
age = int(input("Sisesta oma vanus: "))
if len(name) < age or age > 5:
    for i in range(3):
        print("Tere", name + "!")
else:
    number1 = int(input("Sisesta esimene arv: "))
    number2 = int(input("Sisesta teine arv: "))
    number3 = int(input("Sisesta kolmas arv: "))
    sum_answer = int(input(
        "Siseta arvude " + str(number1) + " " + str(number2) + " " + str(
            number3) + " " + " summa: "))
    if sum_answer == (number1 + number2 + number3):
        print("Õige vastus")
    else:
        print("Vale vastus")