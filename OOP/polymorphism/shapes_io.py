class Shape:
    def show(self):
        print("This is a shape")

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))

    @classmethod
    def load(cls, filename):
        with open(filename, "r") as f:
            data = f.read()
        return data

class Rectangle(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Rectangle sizes: {self.x}x{self.y}")

    def __str__(self):
        return f"Rectangle sizes: {self.x}x{self.y}"

class Cylinder(Shape):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def show(self):
        print(str(self))

    def __str__(self):
        return f"Cylinder with radius={self.r}, height={self.h}, volume={self.volume()}"

    def volume(self):
        return 3.14 * self.r ** 2 * self.h

r = Rectangle(5, 10)
c = Cylinder(3, 7)

r.show()
c.show()

r.save("rect.txt")
c.save("cyl.txt")

print(Rectangle.load("rect.txt"))
print(Cylinder.load("cyl.txt"))
