names = set()

while True:
    new_name = input("Enter a name, or an empty string to quit\n")
    if new_name == "":
        break
    else:
        if new_name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(new_name)

for n in names:
    print(n)