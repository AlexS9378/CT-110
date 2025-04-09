# Alex Sweat
# 4/9/25
# P2LAB1
# The program will calculate the diameter, circumference, and area of a circle.

# Prompt Enter radius of circle
radius = float(input("Enter radius of circle:"))

#Prompt Calculating the diameter of circle
def calculate_diameter(radius):
    return 2 * radius
diameter = calculate_diameter(radius)
form_diameter = round(diameter, 1)
print(f"The Diameter of the circle is {form_diameter}.")

#Prompt Calculating the circumference of circle
pi_value = 3.141592
def calculate_circ(radius):
    return 2 * pi_value * radius
circ = calculate_circ(radius)
form_circ = round(circ, 2)
print(f"The Circumference of the circle is {form_circ}.")

#Prompy Calculating the area if circle
def calculate_area(radius):
    return pi_value * radius ** 2
area = calculate_area(radius)
form_area = round(area, 3)
print(f"The Area of the circle is {form_area}.")
