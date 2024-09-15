seasons = ("Winter", "Spring", "Summer", "Autumn")
request = int(input("ENTER NUMBER OF MONTH AND I SHALL RETURN THE SEASON\n"))

if request in (12, 1, 2):
    print(seasons[0])
elif request in (3, 4, 5):
    print(seasons[1])
elif request in (6, 7, 8):
    print(seasons[2])
elif request in (9, 10, 11):
    print(seasons[3])
else:
    print("invalid number")