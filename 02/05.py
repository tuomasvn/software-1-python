print("This program will convert talents, pounds and lots into kilograms and grams.")
talents = input("Enter the amount of talents: ")
pounds = input("Enter the amount of pounds: ")
lots = input("Enter the amount of lots: ")

talent_lots = float(talents) * 20 * 32
pound_lots= float(pounds) * 32
final_lots = float(lots) + pound_lots + talent_lots

grams = final_lots * 13.3
kilograms = grams / 1000
final_grams = f"{grams % 1000:3.2f}"

print(f"{talents} talent(s), {pounds} pound(s) and {lots} lot(s) weigh {str(int(kilograms))} kilograms and {final_grams} grams.")
