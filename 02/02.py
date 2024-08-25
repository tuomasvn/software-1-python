import math
radius = input("This program will calculate the area of a circle to 3 decimal points. Enter the radius of the circle: ")
area = math.pi * float(radius) ** 2
print(f"The area of a circle with a radius of {radius} is {float(area):.3f}")
