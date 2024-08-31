import random
your_number = 0
random_number = random.randint(1,10)

while your_number != random_number:
    your_number = int(input("Guess the number [1, 10] \n"))

    if your_number > 10:
        print("Way too high! (out of range)")
    elif your_number < 0:
        print("Way too low! (out of range)")
    elif your_number < random_number:
        print("Too low!")
    elif your_number > random_number:
        print("Too high!")
    elif your_number == random_number:
        print("Correct!")
