# Alex Sweat
# 4/29/2025
# P4HW2
# Employee Pay Calculator Modified


total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("Enter employee's name (or type 'Done' to terminate: ")
    
    if employee_name.strip().lower() == "done":
        break  

    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter pay rate: "))

    regular_hours = 40
    overtime_multiplier = 1.5

    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        regular_pay = regular_hours * pay_rate
        overtime_pay = overtime_hours * pay_rate * overtime_multiplier
    else:
        overtime_hours = 0
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0

    gross_pay = regular_pay + overtime_pay

    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay
    employee_count += 1

print(f"Total number of employees entered : {employee_count}")
print(f"Total amount paid for regular hours       : ${total_regular_pay:.2f}")
print(f"Total amount for overtime                 : ${total_overtime_pay:.2f}")
print(f"Total amount paid in gross                : ${total_gross_pay:.2f}")
