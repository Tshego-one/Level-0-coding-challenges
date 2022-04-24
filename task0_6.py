def max_number(a, b, c):

    if a > b and c:
        maximum = a
    elif b > a and c:
        maximum = b
    elif c > a and b:
        maximum = c

    return maximum

print(max_number(1, 22, 3))