import math

def area_circumference(radius):
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    return area, circumference

area, circumference = area_circumference(2)
print("Area:", round(area, 2),"Circumference:", round(circumference, 2))