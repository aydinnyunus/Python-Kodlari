print("-" * 30)
print("1- Celsius to fahrenheit")
print("2- Fahrenheit to celsius")
print("-" * 30)

choice = input("Your choice (1/2): ")

if choice == "1":
    print("\n# Celsius to Fahrenheit")
    celsius = float(input("Degree to convert: "))
    fahrenheit = (celsius * 1.8) + 32
    print("{} degree celsius is equal to {} degree fahrenheit.".format(celsius, fahrenheit))
elif choice == "2":
    print("\n# Fahrenheit to Celsius")
    fahrenheit = float(raw_input("Degree to convert: "))
    celsius = (fahrenheit - 32) / 1.8
    print("{} degree fahrenheit is equal to {} degree celsius.".format(fahrenheit, celsius))
else:
    print("Congratulations! You hacked the super-program.")
