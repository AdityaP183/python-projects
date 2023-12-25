# Convert Celsius to Fahrenheit.
user_choice = int(input("Choose from which to convert:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n"))

if user_choice == 1:
    celsius = float(input("Enter temperature in celcius: "))
    fahrenheit = ((9/5) * celsius) + 32
    print(f"Temperature in fahrenheit: {fahrenheit:.2f}")
elif user_choice == 2:
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (5/9) * (fahrenheit - 32)
    print(f"Temperature in celsius: {celsius:.2f}")