"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse
kraadides ja väljastab tulemuse Fahrenheiti kraadides.
Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui
teistpidi? Proovi.
"""

temperatue = float(input('Siseta temperatuur: '))
unit = input('Mis ühikutes c/f/k: ')
result_unit = input('Mis ühikusse soovid teisentada c/f/k: ')

if unit.lower() == result_unit.lower():
    print(f'{temperatue} {unit}')
elif unit.lower() == 'c':
    if result_unit.lower() == 'f':
        print(
            f'{temperatue}{unit} on {round(temperatue * 1.8 + 32, 2)}{result_unit}')
    elif result_unit.lower() == 'k':
        print(f'Celsius {temperatue} kelvin on {round(temperatue + 273.15, 2)}')
elif unit.lower() == 'f':
    result_c = (temperatue - 32) / 1.8
    if result_unit.lower() == 'c':
        print(
            f'Fahrenheit {temperatue}  Celsiuses on {round(result_c, 2)}')
    elif result_unit.lower() == 'k':
        print(
            f'Fahrenheit {temperatue}  Kelvin on {round(result_c + 273.15, 2)}')
elif unit.lower() == 'k':
    result_k = temperatue - 273.15
    if result_unit.lower() == 'c':
        print(f'Kelvin {temperatue} Celsius on {round(result_k, 2)}')
    elif result_unit.lower() == 'f':
        print(
            f'Kelvin {temperatue} Fahrenheit on {round(result_k * 1.8 + 32, 2)}')
else:
    print('Sisestasid midagi valesti')