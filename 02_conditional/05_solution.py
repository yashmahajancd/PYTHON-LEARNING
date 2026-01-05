weather = input("Enter weather (Sunny/Rainy/Snowy) : ")

if weather == "Sunny" or weather == "sunny":
    activity = "Go for a Walk."
elif weather == "Rainy" or weather == "rainy":
    activity = "Read a Book."
elif weather == "Snowy" or weather == "snowy":
    activity = "Build a Snowman."
    
print(activity)