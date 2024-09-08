def convert(n):
    lit = n * 3.78541178
    return lit

live = True

while live:

    gallons_str = input("How many gallons?\n")
    if not gallons_str.isalpha() and gallons_str != "":
        gallons = float(gallons_str)
        if gallons >= 0:
            print(f"{gallons} gallon(s) is {convert(gallons):.2f} liters.")
        else:
            live = False