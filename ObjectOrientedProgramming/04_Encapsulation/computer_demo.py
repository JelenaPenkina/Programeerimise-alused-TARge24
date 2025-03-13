class Computer:

    def __init__(self):
        self.name = "Inspiron"
        self.__selling_price = 700

    def sell(self):
        print(f"{self.name} Selling Price: {self.__selling_price}")

    def setSellingPrice(self, price):
        self.__selling_price = price


class GamingComputer(Computer):

    def __init__(self):
        super().__init__()
        self.name = "AlienWare"

c = Computer()
c.sell()

# change the price
c.__selling_price = 1000
c._name = "Latitude"
c.sell()

# setting selling price using setter function
c.setSellingPrice(1000)
c.sell()

gc = GamingComputer()
gc.sell()
gc.name = "ROG"
gc.sell()