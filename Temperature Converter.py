def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number.")

    fahrenheit = (celsius * 9/5) + 32
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number.")

    celsius = (fahrenheit - 32) * 5/9
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(2))
print(celsius_to_fahrenheit(5))
print(celsius_to_fahrenheit(21))
print(fahrenheit_to_celsius(2))
print(fahrenheit_to_celsius(5))
print(fahrenheit_to_celsius(21))