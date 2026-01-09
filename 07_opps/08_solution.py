# Use a property decorator in the Car class to make the model attribute read-only.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        
    @property
    def model(self):
        return self.__model
        
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
        
c = Car("Tata", "Safari")
# c.model = "Nexon"
print(c.model)