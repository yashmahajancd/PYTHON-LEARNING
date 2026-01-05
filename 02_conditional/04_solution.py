fruit = input("Enter Fruit Name (e.g. Banana) : ")    #Banana
color = input("Enter the color (Green/Yellow/Brown) : ")    #Yellow

if fruit == "Banana" or fruit == "banana" or fruit == "BANANA":
    if color == "Green" or color == "green" or color == "GREEN":
        print("Unripe")
    elif color == "Yellow" or color == "yellow" or color == "YELLOW":
        print("Ripe")
    elif color == "Brown" or color == "brown" or color == "BROWN":
        print("Overripe")
    else:
        print("Invalid Color!")
else:
    print("Fruit is not available!")