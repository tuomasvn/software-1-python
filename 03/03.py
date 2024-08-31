morf = input("Male or Female (CaSe SeNsItIvE)\n")

hemoglobinvalue = "Your hemoglobin value is"
low = "lower than normal."
high = "higher than normal."

if morf == "Male" or morf == "Female":
    hemoglobin = int(input("What is your hemoglobin value?\n"))

    if morf == "Female" and hemoglobin < 117:
        print(f"{hemoglobinvalue} {low}")
    elif morf == "Female" and (117 <= hemoglobin <= 155):
        print(f"{hemoglobinvalue} normal.")
    elif morf == "Female" and hemoglobin > 155:
        print(f"{hemoglobinvalue} {high}")

    elif morf == "Male" and hemoglobin < 134:
        print(f"{hemoglobinvalue} {low}")
    elif morf == "Male" and (134 <= hemoglobin <= 167):
        print(f"{hemoglobinvalue} normal.")
    elif morf == "Male" and hemoglobin > 167:
        print(f"{hemoglobinvalue} {high}")
    else:
        print("Invalid value.")
else:
    print("Sorry, this program needs you to select 'Male' or 'Female'.")

