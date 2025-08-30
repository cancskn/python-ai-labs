class Human:
    def __init__(self, name= "", birthdate= "", contact= "", city= "", country= "", address= ""):
        self.name = name
        self.birthdate = birthdate
        self.contact = contact
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.name = input("Name: ")
        self.birthdate = input("Date of birth: ")
        self.contact = input("Contact: ")
        self.city = input("City: ")
        self.country = input("Country: ")
        self.address = input("Address: ")


    def show_data(self):
        print(f'Hi, {self.name} here. I was born in {self.birthdate}. '
              f'My contact: {self.contact}. I live in {self.city}, {self.country}. My address: {self.address}.')

human1 = Human()
human1.input_data()
human1.show_data()