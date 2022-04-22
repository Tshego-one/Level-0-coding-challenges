def max_num(a, b, c, d):

    if a > b and c and d:
        maximum = a
    elif b > a and c and d:
        maximum = b
    elif c > a and b and d:
        maximum = c
    elif d > a and b and c:
        maximum = d
    return maximum

print(max_num(1, 22, 3, 2))