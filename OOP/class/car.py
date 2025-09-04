
class Car:
    all_cars = []

    def __init__(self, model, release_year, manufacturer, engine, color, price):
        self.model = model
        self.release_year = release_year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color =  color
        self.price = price
        Car.all_cars.append(self)

    @classmethod
    def show_menu(cls):
        while True:
            print(f"\n Menu")
            print(f" 1 -> Show all cars")
            print(f" 2 -> Filter with price")
            print(f" 3 -> Filter with year")
            print(f" 4 -> Add car")
            print(" 0 -> Exit")
            choice = int(input(" Please make your choice (0-4): "))
            cls.process(choice)

    @classmethod
    def add_car(cls):
        model = input("Model: ")
        release_year = int(input("Release year: "))
        manufacturer = input("Manufacturer: ")
        engine = input("Engine: ")
        color = input("Color: ")
        price = int(input("Price: "))
        cls(model, release_year, manufacturer, engine, color, price)
        print("Car added.")

    @classmethod
    def process(cls, choice):
        if choice == 1:
            print("\n All Cars")
            for car in cls.all_cars:
                print(f"{car.model} {car.release_year}, {car.price}")
        elif choice == 2:
            max_price = int(input("Enter a max price to filter: "))
            for car in cls.all_cars:
                if car.price <= max_price:
                    print(f"{car.model} {car.release_year}, {car.price}")
        elif choice == 3:
            min_year = int(input("Enter a min release year: "))
            for car in cls.all_cars:
                if car.release_year >= min_year:
                    print(f"{car.model} {car.release_year}, {car.price}")
        elif choice == 4:
            cls.add_car()
        else:
            print("Wrong input, try again")

if __name__ == "__main__":
    Car("Ford Mustang", 1970, 'Ford', '300 hp', 'red', 30000)
    Car('Lada Nive', 2010, 'Lada', '250', 'white', 25000)
    Car('Toyota Land', 2025, 'Toyota', '340 hp', 'black', 50000)

    Car.show_menu()













