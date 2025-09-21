class Money:
    def __init__(self, units=0, fraction=0, currency="PLN"):
        self.units = units
        self.fraction = fraction
        self.currency = currency

    def set_units(self, value):
        self.units = value

    def set_fraction(self, value):
        self.fraction = value

    def __str__(self):
        return f"{self.units}.{self.fraction:02d} {self.currency}"

class Product(Money):
    def __init__(self, name, units=0, fraction=0, currency="PLN"):
        super().__init__(units, fraction, currency)
        self.name = name

    def decrease_price(self, amount):
        # convert into fraction
        total_as_fraction = self.units * 100 + self.fraction
        total_as_fraction -= amount

        if total_as_fraction < 0:
            total_as_fraction = 0

        # back to units.fraction
        self.units = total_as_fraction // 100
        self.fraction = total_as_fraction % 100

    def __str__(self):
        return f"{self.name}: {self.units}.{self.fraction:02d} {self.currency}"


p = Product("Water", 2, 50, "EUR")
print(p)

p.decrease_price(50)
print(p)