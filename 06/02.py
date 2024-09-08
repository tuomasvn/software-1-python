def roll(n):
    return random.randint(1, n)

import random
roll_count = 0

top_number_str = input("How many sides does the die have?\n")

if top_number_str.isnumeric() and top_number_str != "0":
    top_number = int(top_number_str)

    while True:
        roll_value = roll(top_number)
        roll_count += 1
        print(roll_value)

        if roll_value == top_number:
            break

    print(f"wohoo! we got a(n) {top_number} after {roll_count} roll(s)!")

else:
    print("invalid input")
