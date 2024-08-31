not_empty_string = True
number_str = input("Enter a number: ")
number = biggest_number = smallest_number = float(number_str)
while not_empty_string:

    number_str = input("Enter a number: ")

    if number_str == "":
        not_empty_string = False

    else:
        number = float(number_str)
        if number > biggest_number:
            biggest_number = number
            print("bigger number than before")

        if number < smallest_number:
            smallest_number = number
            print("smaller number than before")

print(f"The biggest number you entered was {biggest_number}")
print(f"The smallest number you entered was {smallest_number}")
