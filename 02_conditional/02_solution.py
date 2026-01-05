age = int(input("Give me Your Age: "))
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Your Ticket Price is : $",price)