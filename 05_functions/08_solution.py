# def print_kwargs(name, power):
#     print("Name :", name, "\tPower :", power)
    
# print_kwargs(name = "Shaktiman", power = "Lazer")    # Name : Shaktiman        Power : Lazer
# print_kwargs(power = "Lazer", name = "Shaktiman")    # Name : Shaktiman        Power : Lazer
# print_kwargs(name = "Shaktiman")                     # Erron -------------------
# print_kwargs(power = "Lazer", name = "Shaktiman", enemy = "Dr. Jackaal")   # Erron --------

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
print("----------------------------")
print_kwargs(name = "shaktiman", power = "lazer")
print("----------------------------")
print_kwargs(power = "lazer", name = "shaktiman")
print("----------------------------")
print_kwargs(name = "shaktiman")
print("----------------------------")
print_kwargs(id = "001", name = "Ram", age = "21")
print("----------------------------")