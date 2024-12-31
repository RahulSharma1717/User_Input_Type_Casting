# Take Temperature in celsius and convert it into fahreinheit.
# Hint: the formula for converting Celsius to Fahrenheit is F = (C * 9/5) + 32

temp_celsius = float(input("Please Enter Temperature in Celsius: "))
fahrenheit = (temp_celsius * 9/5) + 32
print("Temperature in fahrenheit:", fahrenheit)


"""Output:
Please Enter Temperature in Celsius: 37.7
Temperature in fahrenheit: 99.86"""



# Take Temperature in fahreinheit and convert it into celcius.

temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (temp_fahrenheit - 32) * 5/9
print(f"{temp_fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")


"""Output:
Enter temperature in Fahrenheit: 98.6
98.6 degrees Fahrenheit is equal to 37.0 degrees Celsius."""
