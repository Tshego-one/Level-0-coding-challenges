def area_of_triangle(side1, side2, side3):

    s = (side1 + side2 + side3) / 2
    area = ((s*(s-side1)*(s-side2)*(s-side3)))**(1/3)
    return area
print(area_of_triangle(2, 3, 4))