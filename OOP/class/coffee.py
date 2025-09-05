class CoffeeMachine:
    def __init__(self, coffee_beans, milk, sugar, water):
        self.coffee_beans = coffee_beans
        self.milk = milk
        self.sugar = sugar
        self.water =water

    def make_espresso(self):
        if self.coffee_beans >= 50 and self.water >= 100:
            self.coffee_beans -= 50
            self.water -= 100
            print("Enjoy your espresso")
        else:
            print("You dont have enough resources")

    def make_cappucino(self):
        if self.coffee_beans >= 40 and self.milk >= 100 and self.water >= 100:
            print("Enjoy your cappucino")
            self.coffee_beans -= 40
            self.milk -= 100
            self.water -= 100

    def make_latte(self):
        if self.coffee_beans >= 30 and self.milk >= 100 and self.water >= 100:
            print("Enjoy your latte")
            self.coffee_beans -= 30
            self.milk -= 100
            self.water -= 100

    def resources(self):
        return {
            "coffee beans": self.coffee_beans,
            "milk": self.milk,
            "water": self.water,
            "sugar": self.sugar
        }


def get_active_machine():
    if machine.coffee_beans > 0 or machine.milk > 0 or machine.water > 0:
         return machine
    else:
        return new_machine

machine = CoffeeMachine(300, 500, 5000, 1000)
new_machine = CoffeeMachine(200, 300, 1000, 1000)

while True:
    print('old machine resources: ' + str(machine.resources()))
    print('new machine resources: ' + str(new_machine.resources()))
    Guest = input('What coffee you want?')

    active_machine = get_active_machine()
    if Guest == 'c':
        active_machine.make_cappucino()
    elif Guest == 'l':
        active_machine.make_latte()
    elif Guest == 'e':
        active_machine.make_espresso()
    else:
        break

