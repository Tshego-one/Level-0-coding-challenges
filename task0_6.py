def max_number(num1, num2, num3):

    if (num1 >= num2) and (num1 >= num3):
        maximum = num1
    elif (num2 >= num1) and (num2 >= num3):
        maximum = num2
    elif (num3 >= num1) and (num3 >= num2):
        maximum = num3

    return maximum

print(max_number(5, 8, 3))