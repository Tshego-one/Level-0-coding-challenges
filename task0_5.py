import math
def area_of_triangle(length1, length2, length3):

    s = (length1 + length2 + length3) / 2
    area = math.sqrt((s*(s-length1)*(s-length2)*(s-length3)))
    return area
print(area_of_triangle(2, 3, 4))