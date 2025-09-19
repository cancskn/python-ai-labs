class Shape:  # abstract class
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

class RightTriangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 0.5 * self.a * self.b

class Trapezoid(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return (self.a + self.b) / 2 * self.h



