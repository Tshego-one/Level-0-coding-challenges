def area_of_triangle(side1, side2, side3):

    semi_perimeter = (side1 + side2 + side3) / 2
    area = ((semi_perimeter*(semi_perimeter - side1)*(semi_perimeter - side2)*(semi_perimeter - side3)))**(1/2)
    return area
print(area_of_triangle(2, 3, 4))