import datetime

test_value = False
user_input_str = input("Enter a positive integer: ")

if user_input_str.isdigit() and user_input_str != "0":
    user_input = int(user_input_str)

    if user_input > 1:
        print(f"Calculating. Start time: {datetime.datetime.now().strftime('%H:%M:%S')}")

        for n in range(2, user_input):
            if user_input % n == 0:
                test_value = True
                print(f"divisible by {n}")
                break

        if test_value:
            print(f"{user_input} is not prime!")

        else:
            print(f"{user_input} is prime!")

        print(f"End time: {datetime.datetime.now().strftime('%H:%M:%S')}")

    else:
        print("1 is not prime!")

else:
    print("invalid input")