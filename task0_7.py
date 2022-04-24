# Converting celsius to fahrenheit
def convert(celsius):

    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit
    
fahrenheit = convert(30)
print(f"{fahrenheit} fahrenheit")

# Converting fahrenheit to celsius
def change(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = change(86)
print(f"{celsius} degrees celsius")
