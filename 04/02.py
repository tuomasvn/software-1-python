inch = 0
positive = True

while positive:
    inch = float(input("How many inches?\n"))

    if inch >= 0:
        in_to_cm = inch * 2.54
        print(f"{inch} inch(es) is {in_to_cm} centimeters.")
    else:
        positive = False

print("oops! you entered a negative number! self destruct initiated!")
