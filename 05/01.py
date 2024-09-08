import random

dice = int(input("How many dice to roll?\n"))

total = 0
for n in range(1, dice + 1):
    total = total + random.randint(1, 6)

print(total)