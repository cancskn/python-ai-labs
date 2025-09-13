import random

class Person:
    membership = True  # class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__personSecret = random.randint(1, 100)  # __ used to make attribute private

    def __personId(self):  # __ used to make method private
        return random.randint(1, 10)
    
    def get_id(self):
        return self.__personId()
    
    def works(self):
        return f"{self.name} is working"

person = Person("John", 30)
#print(person.__personId())  # This will raise an AttributeError
print(person.get_id()) 