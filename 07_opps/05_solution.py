# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def fule_type(self):
        return "Petrol or Diesel"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def fule_type(self):
        return "Electric Charge"
        
e = ElectricCar("Tesla", "S", "85kWh")
print(e.fule_type())

c = Car("Tata", "Safari")
print(c.fule_type())