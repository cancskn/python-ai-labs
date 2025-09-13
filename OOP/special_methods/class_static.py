class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
    @classmethod
    def show_population(cls):
        return f"Current population is {cls.population}"

    @classmethod
    def show_name(cls):
        return cls.name # This will raise an AttributeError since 'name' is not a class attribute
    
    @staticmethod
    def is_adult(age):
        return age >= 18


person = Person("John", 30)
person2 = Person("Alice", 25)

print(person2.show_population())
print(person.is_adult(20))  
# print(Person.show_name())  # This will raise an AttributeError