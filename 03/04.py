year = int(input("Enter a year: "))

if year % 4 == 0:

    if year % 400 == 0:
        print("That is a leap year (Divisible by 400)")
    elif year % 100 == 0:
        print("That is not a leap year (Divisible by 100 but not 400)")
    else:
        print("That is a leap year (Divisible by 4)")

else:
    print("That is not a leap year (Not divisible by 4)")
