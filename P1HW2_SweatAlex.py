# Alex Sweat
# 04/01/2025
# P1HW2
# Creating a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")

#Prompt Enter Budget
base = float(input("Enter Budget:"))

#Prompt Enter Travel Destination
travel = input("Enter your travel desination:")

#Prompt Gas Expenditure
a = float(input("How much do you think you will spend on gas?"))

#Prompt Accommodation Expenditure
b = float(input("Approximately, how much will you need for accommodation/hotel?"))

# Prompt Food Expenditure
c = float(input("Last, how much do you need for food?"))

print("--------Travel Expenses--------")
print("Location:", travel)
print("Initial Budget:", base)

print("Fuel:", a)
print("Accomodation:", b)
print("Food:", c)

#Prompt Add Expenses
def calculate(base, a, b, c):
    return base - (a + b + c)

#Calculate
result = calculate(base, a, b, c)

#Display Result
print(f"Remaining Balance:{result}")
