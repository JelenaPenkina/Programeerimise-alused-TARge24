def elektrihind():
    """Ask user electricity price in s/kWh.

    :return price in €/MWh
    """
    price_cent_kwh = float(
        input('Sisesta elektrihind sentides kilovatt-tunni kohta:'))
    return f'{price_cent_kwh} kWh on {price_cent_kwh * 10} €/MWh'


if __name__ == '__main__':
    print(elektrihind())