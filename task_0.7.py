celsius = int(input("Please input your value: "))

def change(c):
    """
    Converts celsius degress to fahrenheit
    """
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit
    
fahrenheit = change(celsius)
print(f"{fahrenheit} fahrenheit")


fahrenheit = int(input("Please input your value: "))

def change(f):
    """
    Converts fahrenheit to degrees celsius
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = change(fahrenheit)
print(f"{celsius} degrees celsius")
