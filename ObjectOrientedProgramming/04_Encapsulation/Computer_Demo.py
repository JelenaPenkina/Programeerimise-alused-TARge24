class Computer:

    def __init__(self):
        self._name = "Dell"
        self.__selling_price = 700

    def sell(self):
        print(f"{self._name} Selling Price: {self.__selling_price}")

    def set_selling_price(self, price):
        self.__selling_price = price


class Gaming_computer(Computer):
    """Class Gaming"""

    def __init__(self):
        super().__init__()
        self._name = "Gaming"


c = Computer()
c.sell()

# change the price
c.__selling_price = 1000
c.name = "IBM"
c.sell()

# setting selling price using setter function
c.set_selling_price(1000)
c.sell()

gc = Gaming_computer()
gc.sell()
gc._name = "HP"
gc.sell()