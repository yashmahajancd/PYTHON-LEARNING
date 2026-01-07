input_str = input("Enter the string for reverse : ")
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
    
print(reversed_str)