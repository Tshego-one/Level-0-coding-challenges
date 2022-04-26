def change(celsius):

    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit
    
fahrenheit = change(30)
print(f"{fahrenheit} fahrenheit")

#
def convert(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = convert(86)
print(f"{celsius} degrees celsius")
