class Device:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def info(self):
        return f"{self.brand}, power: {self.power}W"

class CoffeeMachine(Device):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity

    def make_coffee(self):
        return f"{self.brand} makes {self.capacity} cups of coffee"

    def info(self):
        return super().info() + f", capacity: {self.capacity} cups"

class Blender(Device):
    def __init__(self, brand, power, type_product):
        super().__init__(brand, power)
        self.type_product = type_product

    def blend(self):
        return f"{self.brand} can blend {self.type_product}"

    def info(self):
        return super().info() + f", Products: {self.type_product}"

class MeatGrinder(Device):
    def __init__(self, brand, power, capacity, blade_num):
        super().__init__(brand, power)
        self.capacity = capacity
        self.blade_num = blade_num

    def grind(self):
        return f"{self.brand} has {self.blade_num} different types of blades"

    def info(self):
        return super().info() + f", Capacity: {self.capacity} gr, Amount of different blades: {self.blade_num}"


bl = Blender("Boss", "400", "Zupa")
print(bl.blend())
print(bl.info())