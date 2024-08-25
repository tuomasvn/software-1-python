print("This program will calculate the perimeter and area of a rectangle of given dimensions.")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

print(f"The perimeter of the rectangle is {length * 2 + width * 2:.3f}")
print(f"The area of the rectangle is {length * width:.3f}")
