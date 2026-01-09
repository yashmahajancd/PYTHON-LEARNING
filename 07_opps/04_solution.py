# Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand + " !"
        
    def disp_car(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
        
c = ElectricCar("Tesla", "S", "85kwh")
print(c.get_brand())
print(c.model)
print(c.battery_size)
print(c.disp_car())