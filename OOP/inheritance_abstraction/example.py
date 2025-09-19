class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
class Student(Person):
    def __init__(self, name, age, student_id, email):
        super().__init__(name, age, email) # Initialize parent class attribute
        self.student_id = student_id
    
    def show_id(self):
        return f"I am {self.name}, and my student ID is {self.student_id}."


person = Person("Alice", 30, "abc@gmail.com")
student = Student("Joe", 20, "S12345", "joe@gmail.com")

print(student.introduce())   # Person's method
print(student.show_id())     # Student's method
print(student.email)         # Person's attribute
