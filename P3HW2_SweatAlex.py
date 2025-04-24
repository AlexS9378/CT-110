# Alex Sweat
# 4/23/2025
# P3HW2
# Employee Pay Calculator

# Get user input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Rates
regular_hours = 40
overtime_rate = 1.5

# Calculate pay
if hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * overtime_rate
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

# Gross pay
gross_pay = regular_pay + overtime_pay

# Display the output

print("\n-----------------------------")
print(f"Employee Name: {employee_name}")
print()
print(f"{'Pay Rate':<12}{'Hours':<8}{'Overtime':<10}"
      f"{'Overtime Pay':<10}  {'RegHour Pay':<10}  {'Gross Pay':<10}")
print("-" * 75)
print(f"{pay_rate:<11.2f} {hours_worked:<8.1f}"
      f"{overtime_hours:<10.1f}{overtime_pay:<9.2f}     {regular_pay:<9.2f}    {gross_pay:<9.2f}")

