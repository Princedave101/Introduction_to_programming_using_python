import math

# Question:
"""
(Compute the volume of a cylinder) Write a program that reads in the radius and
length of a cylinder and computes the area and volume using the following formulas:

area = radius * radius * π
volume = area * length
"""

# Solution:
"""     
    1. Import the math module
    2. Recieve both radius and length  from user
    3. Compute the volume and area of the cylinder using the formulas above(use the pie constant in the math module)
    4. Display the results rounded to n decimal place on the console
"""

radius, length = eval(input("Enter the radius and the length of the cylinder respectively seperated by a comma(eg. 5, 11): "))

area = radius * radius * math.pi
volume = area * length

print("The area is", round(area, 4))
print("The volume is", round(volume, 2))

