## 1) Age Group Categorization

# - Classify a person's age group: Child(<13), Teenager(13-19), Adult(20-59), Senior(60+).

user = int(input("Give me your age: "))

if user < 13:
    print("You are Child")
elif user < 20:
    print("You are Teenager")
elif user < 60:
    print("You are Adult")
else:
    print("You are Senior")