class Vehicle:  # Parent class
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):  # Child class
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

    def display(self):
        print("Car Brand:", self.brand)
        print("Fuel Type:", self.fuel_type)

class Bike(Vehicle):  # Child class
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

    def display(self):
        print("Bike Brand:", self.brand)
        print("Engine CC:", self.engine_cc)

# Take input from user
b1 = input("Enter car brand: ")
f = input("Enter fuel type: ")
b2 = input("Enter bike brand: ")
cc = int(input("Enter engine CC: "))

# Create objects
c = Car(b1, f)
b = Bike(b2, cc)

# Display details
c.display()
b.display()