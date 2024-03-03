class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}\'s engine is starting.")

    def drive(self, distance):
        print(f"The {self.make} {self.model} is driving {distance}km.")

    def stop_engine(self):
        print(f"The {self.make} {self.model}\'s engine is stopping.")


car1 = Car("Toyota", "Supra", 1977)
car2 = Car("Lada", "Niva", 1967)

print(car1.make)
print(car1.model)

car1.start_engine()
car2.start_engine()
car1.drive(150)
car2.stop_engine()
