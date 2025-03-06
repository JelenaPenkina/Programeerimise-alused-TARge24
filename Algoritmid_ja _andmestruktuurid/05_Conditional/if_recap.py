"""
Kirjuta programm, mis küsib kasutajalt ilma ja kuupäeva ning
olenevalt vastusest kirjutab erineva tegevuse ekraanile.

Kasutame liit tingimust ja vähemalt kolme erinevat tegevust.
"""


def askUser(Weather, Date) -> str:
    if (Weather == "Sunny"):
        print(f"What weather today is: {Weather}.")
        return "Sunny"
    elif (Date == "Monday"):
        print(f"What date today is: {Date}.")
        return "Monday"
    else:
        return "It´s not what we ask."


# def askWeather(Weather) -> str:
#   if():
#       print(f"What weather it is:" + Weather)
#       return Weather


rainy = "vihmane"
date_before_christmas = "20.12.2024"  # shift+F6 -> muudab ära igal pool muutuja
date_in_autumn = "10.10.2025"

weather = input("Milline ilm on?")
date = input("Mis on kuupäev?")

if weather == rainy and date == date_before_christmas:
    print("Pole eriti talvine ilm, aga jalutada võib ikka.")
elif weather == rainy and date == date_in_autumn:
    print("Ilus sügisilm, mine porilompi hüppama.")

if weather == rainy:
    if date == "20.12.2024":
        print("Pole eriti talvine ilm, aga jalutada.")
    elif date == "10.10.2025":
        print("Ilus sügisilm, mine porilompi hüppama.")

if __name__ == "__main__":
    assert askUser("Raining", "Tuesday") == "It´s not what we ask"
    assert askUser("Sunny", "Monday") == "Sunny"
    assert askUser("Raining", "Monday") == "Monday"
    print("OK")
