# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
class ElecricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
my_tesla = ElecricCar("Tesla", "Model S", "85kWh")
my_tata = Car("Tata", "Nexon")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElecricCar))
print(isinstance(my_tata, ElecricCar))
print(isinstance(my_tata, Car))