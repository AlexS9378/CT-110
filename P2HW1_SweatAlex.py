# Alex Sweat
# 04/09/2025
# P2HW1
# Creating a program that does some basic math on numbers that are entered

print("This program calculates and displays travel expenses")
print()

#Prompt Enter Budget
base = float(input("Enter Budget:"))
print()

#Prompt Enter Travel Destination
travel = input("Enter your travel desination:")
print()

#Prompt Gas Expenditure
a = float(input("How much do you think you will spend on gas?"))
print()

#Prompt Accommodation Expenditure
b = float(input("Approximately, how much will you need for accommodation/hotel?"))
print()

# Prompt Food Expenditure
c = float(input("Last, how much do you need for food?"))
print()

print("--------Travel Expenses--------")

print(f"{'Location:':<18} {travel}")
print(f"{'Initial Budget:':<18} ${base:.2f}")
print(f"{'Fuel:':<18} ${a:.2f}")
print(f"{'Accommodation:':<18} ${b:.2f}")
print(f"{'Food:':<18} ${c:.2f}")

print("-------------------------------")
print()

#Prompt Add Expenses
def calculate(base, a, b, c):
    return base - (a + b + c)

#Calculate
result = calculate(base, a, b, c)

#Display Result
print(f"{'Remaining Balance:':<10} ${result:.2f}")
