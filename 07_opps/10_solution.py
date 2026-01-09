# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar("Tesla", "Model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())