# Dunder (double underscore) methods are special built-in methods in Python
# Example: __init__ (constructor), __str__ (string representation), __len__ (length)

class Costum:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def total(self):
        return f"total= {self.num1 + self.num2}"

    def __len__(self):
        return 2
    
    def __str__(self):
        return "this is a custom string method"

custom = Costum(10, 20)

print(custom.total())  
print(len(custom.total()))  # Output: 9, beacause "total= 30" has 9 characters
print(len(custom)) # Output: 2, because takes it from customized __len__ method
print(custom) # Output: this is a custom string method
print(str(custom)) # Output: this is a custom string method