import math
def area_of_triangle(a, b, c):

    perimeter = a + b + c
    s = (a + b + c) / 2
    area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    return area
print(area_of_triangle(2, 3, 4))