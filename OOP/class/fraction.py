class Fraction:
    def __init__(self, numerator=0, denominator=0):
        self.numerator = numerator
        self.denominator = denominator
        self.num1 = None
        self.num2 = None

    def get_num(self):
        self.numerator = int(input('numerator: '))
        self.denominator = int(input('denominator: '))
        self.num1 = self.numerator / self.denominator
        self.num2 = self.denominator / self.numerator

    def arithmetic_op(self):
        operation = int(input('1.add, 2.subs 3.multiply\n'))
        if operation == 1:
            result = self.num1 + self.num2
        elif operation == 2:
            result = self.num1 - self.num2
        elif operation == 3:
            result = self.num1 * self.num2
        else:
            result = None
        print('Number1: ', self.num1)
        print('Number1: ', self.num2)
        print('Result:', result)


frac = Fraction()
frac.get_num()
frac.arithmetic_op()
