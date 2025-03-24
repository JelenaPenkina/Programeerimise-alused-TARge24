"""
Kirjuta programm, mis küsib kasutajalt ilma ja kuupäeva ning
olenevalt vastusest kirjutab erineva tegevuse ekraanile.

Kasutame liit tingimust ja vähemalt kolme arinevat tegevust
"""
from datetime import datetime

date_format = "%d.%m.%Y"
rainy = 'sajab'

weather = str(input("Mis ilm õues on? "))
askedDate = input("Mis Kuu on? ")

askedDate = datetime.strptime(askedDate, date_format)

if weather.lower() == rainy and askedDate < datetime.now():
    print('Võta vihmavari kaasa')
    if askedDate.month > 9 or askedDate.month < 3:
        print('Paha suusailm')
    else:
        print('Käib kah')
elif weather.lower() == 'päike':
    print('Vihmavarju pole vaja')
else:
    print('Mingi imelik ilm')