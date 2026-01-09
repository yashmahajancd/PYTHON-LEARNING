# Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
c1 = Car("Tata", "Safari")
print(c1.brand)
print(c1.model)

c2 = Car("Toyota", "Corolla")
print(c2.model)
print(c2.brand)