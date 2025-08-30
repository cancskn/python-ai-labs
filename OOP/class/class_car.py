class Car:
    def __init__(self, body, engine, model):
        self.body = body
        self.engine = engine
        self.model = model

    def prints_specification(self, speed):
        print(f"this car runs at speed of {speed} km/h")

# car = Car("Hyundai", 3000, "tucson")
# car1 = Car("Mercedes", 2500, "maybach")
#
# car.prints_specification(200)


