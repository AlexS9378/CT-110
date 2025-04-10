# Alex Sweat
# 04/09/2025
# P2HW2
# Design a program to store and calculate grades

module_grades = []

grade1 = float(input("Enter grade for Module 1:"))
grade2 = float(input("Enter grade for Module 2:"))
grade3 = float(input("Enter grade for Module 3:"))
grade4 = float(input("Enter grade for Module 4:"))
grade5 = float(input("Enter grade for Module 5:"))
grade6 = float(input("Enter grade for Module :"))

module_grades.extend([grade1, grade2, grade3, grade4, grade5, grade6])

low = min(module_grades)
high = max(module_grades)
total = sum(module_grades)
avrg = total / len(module_grades)

print()
print("----------Results----------")
print(f"{'Lowest Grade:':<15} {low:.2f}")
print(f"{'Highest Grade:':<15} {high:.2f}")
print(f"{'Sum of Grades:':<15} {total:.2f}")
print(f"{'Average:':<15} {avrg:.2f}")
print("---------------------------")
