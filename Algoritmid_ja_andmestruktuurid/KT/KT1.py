"""
 Küsi kasutajalt 3 arvu
2.       Väikseim arv korruta kahega
3.       Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
4.       Teata kas kasutaja vastas õigesti või valesti
5.       Teata mitu korda kasutaja vastas õigesti.
"""

import math

"""Ask for input"""
number1 = int(input("Siseta üks arv:"))
number2 = int(input("Siseta teine arv:"))
number3 = int(input("Sisesta kolmas arv:"))

"""Will add all numbers to array"""
numbers = [number1, number2, number3]
numbers.sort()
numbers = [number1 * 2, number2, number3]
print(numbers)

request_until = 1
while request_until < numbers[0]:
    input_result = int(input("Sisesta arv " + str(request_until) + " ruudus: "))
    if input_result == int(math.pow(request_until, 2)):
        print(math.pow(request_until, 2))
        print("Õige vastus")
        request_until += 1
    else:
        print("Vale vastus")