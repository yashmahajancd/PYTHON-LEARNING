species = input("Enter Pet Species (Dog/Cat) : ").lower()
age = int(input("Enter age of pet (years) : "))

food = None

if species == "dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif species == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Junior cat food"
else:
    print("Pet is NOT available!")
    
print("Recommended Food : ", food)