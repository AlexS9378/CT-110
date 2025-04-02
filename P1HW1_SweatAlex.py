# Alex Sweat
# 04/01/2025
# P1HW1
# Using pythons input and print functions to create a program dealing with intergers and calculations.

# Prompt Calculating Exponents
print(f"----Calculating Exponents----")

#Prompt Enter Interger as Base Value/Exponent
base = float(input("Enter an interger as the base value:"))
exponent =float(input("Enter an interger as the exponent:"))

#Calculation
result = base ** exponent

#Print result
print(f"{base} raised to the power of {exponent} is {result}!!")

#Prompt Addition and Subtraction
print(f"----Addition and Substraction----")

#Prompt Enter Interger as Starting/Add/Subtract
base = float(input("Enter a starting interger:"))
add = float(input("Enter an integer to add:"))
subtract = float(input("Enter an interger to subtract:"))

def calculate(base, add, subtract):
    return base + add - subtract

#Calculation
result = calculate(base, add, subtract)

#Print result
print(f"{base} + {add} - {subtract} is equal to {result}")
