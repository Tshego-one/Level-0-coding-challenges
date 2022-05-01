def convert_celsius(celsius):

    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit
    
fahrenheit = convert_celsius(30)
print(f"{fahrenheit} fahrenheit")


def convert_fahreneit(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = convert_fahreneit(86)
print(f"{celsius} degrees celsius")
