# This has a lot of extra stuff, I was testing time taken between computers

import random
import datetime

inside_circle = 0

print("This program will calculate pi from random points with some math.")
point_amount = point_counter = int(input("How many random points do you want to generate?\n"))

print(f"Calculating. Start time: {datetime.datetime.now().strftime('%H:%M:%S')}")

while point_counter > 0:

    # not needed, prints out progress with very large amounts
    if point_counter % 2000000 == 0 and inside_circle != 0:
        print(f"Still calculating... ({((point_amount - point_counter) / point_amount) * 100:.2f}% done)")

    point_x = random.uniform(-1, 1)
    point_y = random.uniform(-1, 1)
    point_counter -= 1

    if point_x ** 2 + point_y ** 2 < 1:
        inside_circle += 1

print(f"of {point_amount} points, {inside_circle} of them are inside the circle")
print(f"-> pi is about {4 * (inside_circle / point_amount)}")

print(f"End time: {datetime.datetime.now().strftime('%H:%M:%S')}")