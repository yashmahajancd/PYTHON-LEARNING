distance = float(input("Enter Distance (km) : "))

if distance < 3:
    mode = "Walk"
elif distance <= 15:
    mode = "Bike"
else:
    mode = "Car"
    
print("Transportation Mode : ", mode)