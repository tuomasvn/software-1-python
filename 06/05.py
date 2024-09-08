def un_uneven(list):
    even_list = []

    for n in list:
        if n % 2 == 0:
            even_list.append(n)

    return even_list
'''
number_list = []

while True:
    new_number = input("Enter a number: ")

    if new_number == "":
        break

    else:
        number_list.append(int(new_number))

new_list = un_uneven(number_list)
print(f"Original list: {number_list}")
print(f"New list: {new_list}")
'''