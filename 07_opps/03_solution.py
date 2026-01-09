# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display(self):
        return f"{self.brand} {self.model}".upper()

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
    def disp(self):
        return f"{self.display()} {self.battery_size}"
        
e1 = ElectricCar("Tesla", "Model S", "85kWh")
print("Brand :",e1.brand)
print("Model :",e1.model)
print("Battery Size :",e1.battery_size)
print(e1.disp())
print(e1.display())