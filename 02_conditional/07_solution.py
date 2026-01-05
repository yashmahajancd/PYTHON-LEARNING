order_size = input("Enter a Coffee order size (Small/Medium/Large) : ")
extra_shot = input("Do you want to add an Extra shot (Yes/No) : ")

if extra_shot == "Yes" or extra_shot == "yes":
    coffee = order_size + " coffee with extra shot."
else:
    coffee = order_size + " coffee"
    
print("Order : ", coffee)