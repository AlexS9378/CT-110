# Alex Sweat
# 4/29/2025
# P4HW1
# Modified P2HW2 code


while True:
    try:
        num_grades = int(input("How many grades would you like to enter? "))
        if num_grades > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

module_grades = []

for i in range(1, num_grades + 1):
    while True:
        try:
            grade = float(input(f"Enter grade for Module {i}: "))
            if 0 <= grade <= 100:
                module_grades.append(grade)
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")

# Calculations
low = min(module_grades)
high = max(module_grades)
total = sum(module_grades)
avrg = total / len(module_grades)

# Modified List
modified_grades = module_grades.copy()
modified_grades.remove(low)

# Letter Grade
if avrg >= 90:
    letter = "A"
elif avrg >= 80:
    letter = "B"
elif avrg >= 70:
    letter = "C"
elif avrg >= 60:
    letter = "D"
else:
    letter = "F"

print("\n----------Results----------")
print(f"{'Lowest Grade:':<20} {low:.2f}")
print(f"{'Modified Grades:':<20} {modified_grades}")
print(f"{'Average:':<20} {avrg:.2f}")
print(f"{'Letter Grade:':<20} {letter}")
print("---------------------------")
