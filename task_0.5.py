import math
a = int(input("Please input side a: "))
b = int(input("Please input side b: "))
c = int(input("Please input side c: "))

def area_of_triangle():
    """
    Prints out the area of a traingle using three sides by using Heron's formula
    to the calculate the area
    """
    perimeter = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return area
print(area_of_triangle())