numbers = []
user_input = "test"

while user_input != "":
    user_input = input("Write number or press enter: ")

    if user_input != "":
        numbers.append(int(user_input))

numbers.sort(reverse=True)

if len(numbers) >= 5:
    for n in range(0, 5):
        print(numbers[n])
else:
    print("Not enough numbers")