from OOP.inheritance_abstraction.shape import Shape

class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Square has equal sized of edges with {self.a}, and area = {self.area()}"

s = Square(10)
print(int(s))
print(s)