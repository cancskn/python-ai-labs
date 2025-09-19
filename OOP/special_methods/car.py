class Car:
    def __init__(self, brand, has_fuel = False):
        self.brand = brand
        self.has_fuel = has_fuel

    def __bool__(self):
        return self.has_fuel

    def __str__(self):
        if self: # __bool__ is called here
            return f"{self.brand} has fuel. Car can start"
        else:
            return f"{self.brand} has no fuel. Car cannot start"

car1 = Car("Opel")
car2 = Car("Fiat", has_fuel=True)
print(str(car1))
print(str(car2))