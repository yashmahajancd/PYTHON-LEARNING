import math

def circule_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circule_stats(3)

print(f"Area : {a:.2f}\nCircumference : {c:.2f}")