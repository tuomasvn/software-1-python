def roll():
    return random.randint(1,6)

import random
is_six = False
roll_count = 0

while True:
    roll_value = roll()
    roll_count += 1
    print(roll_value)

    if roll_value == 6:
        break

print(f"wohoo! we got a 6 after {roll_count} roll(s)!")