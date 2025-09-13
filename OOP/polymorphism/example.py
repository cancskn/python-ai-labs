# Same method but different behavior

class Human:
    def __init__(self, name):
        self.name = name
    
    def attack(self, weapon):
        return f"{self.name} attacks with power of : {weapon}"
    
class Animal:
    def __init__(self, name):
        self.name = name
    
    def attack(self, power):
        return f"{self.name} attacks with power of : {power}"

person = Human("John")
animal = Animal("Lion")
animal2 = Animal("Hyena")

print(person.attack("Sword"))
print(animal.attack("Claws"))
print(animal2.attack("Teeth"))

entities = [Human('Ted'), Human('Joe'), Animal('Cat')]
weapon = ["Sword", "Bow", "Spear"]

for e in entities:
    if isinstance(e, Human):
        print(e.attack(weapon.pop()))
    elif isinstance(e, Animal):
        print(e.attack("Sharp Claws"))