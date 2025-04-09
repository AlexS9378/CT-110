# Alex Sweat
# 4/9/25
# P2LAB2
# How to write code that uses a dictionary to store user input and displays output to the user

my_dict = {
    'Camaro': 18.21,
    'Prius': 52.37,
    'Model S': 110,
    'Silverado': 26
}
print(my_dict)

model = input("Enter a vehicle to see it's MPG:")

mpg = my_dict.get(model)

print(f"The {model} gets {mpg} mpg.")

mile = float(input(f"How many miles will you drive the {model}:?"))
gas = mile / mpg
gas_needed = round(gas, 2)
print(f"{gas_needed} gallon(s) of gas are needed to drive the {model} {mpg} mile(s).")
