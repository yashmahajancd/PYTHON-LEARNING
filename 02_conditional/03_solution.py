score = int(input("Enter your Score: "))

if score >= 101 or score < 0:
    print("Please verify your grade again")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    
print("Grade : ", grade)


# if score >= 90 and score <= 100:
#     print("A Grade")
# elif score >= 80 and score <= 89:
#     print("B Grade")
# elif score >= 70 and score <= 79:
#     print("C Grade")
# elif score >= 60 and score <= 69:
#     print("D Grade")
# elif score <= 59 and score > 0:
#     print("F Grade")
# else:
#     print("Please enter 1-100.")