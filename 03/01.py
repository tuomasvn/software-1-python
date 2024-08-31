length = float(input("How many centimeters long is the zander you caught?\n"))
if length >= 42:
    print("Oh. I guess you can keep it.")
else:
    print(f"Oh no! You need to release it back into the lake! It was {42 - length}cm too short!")