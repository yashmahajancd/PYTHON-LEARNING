# Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
c1 = Car("Tata", "Safari")
c2 = Car("Tata", "Nexon")
e1 = ElectricCar("Tesla", "S", "85kWh")

print(Car.total_car)