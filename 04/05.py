correct_credentials = False
attempt = 1

while attempt < 6 and not correct_credentials:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "python" and password == "rules":
        correct_credentials = True
    else:
        attempt += 1

if correct_credentials:
    print("Welcome")

elif attempt == 6:
    print("Access denied")
