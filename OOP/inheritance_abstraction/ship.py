class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def info(self):
        return f"Ship: {self.name}, Length: {self.length}"

class Frigate(Ship):
    def __init__(self, name, length, speed):
        super().__init__(name, length)
        self.speed = speed

    def info(self):
        return super(). info() + f", Speed: {self.speed} km/h"

class Destroyer(Ship):
    def __init__(self, name, length, power):
        super(). __init__(name, length)
        self.power = power

    def attack(self):
        return f"{self.name} attacks with {self.power} power"

    def info(self):
        return super(). info() + f", Attack power: {self.power}"

class Cruiser(Ship):
    def __init__(self, name, length, capacity):
        super().__init__(name, length)
        self.capacity = capacity

    def info(self):
        return super(). info() + f", Capacity: {self.capacity} m^2"


d = Destroyer("Boo", 640, 90)
print(d.attack())
print(d.info())