import math

def pizza_price(diameter, price):
    area = math.pi * ((diameter / 2) / 100) ** 2
    print(f"{area:.2f}m²")
    print(f"{price}€")
    return price / area

size_text = "What is the diameter of that pizza (in cm)?\n"
price_text = "How much does that pizza cost (in €)?\n"

diameter1 = float(input(size_text))
price1 = float(input(price_text))
price_per_area1 = pizza_price(diameter1, price1)
print(f"Pizza 1 costs {price_per_area1:.2f} €/m²")

diameter2 = float(input(size_text))
price2 = float(input(price_text))
price_per_area2 = pizza_price(diameter2, price2)
print(f"Pizza 2 costs {price_per_area2:.2f} €/m²")

if price_per_area2 > price_per_area1:
    print(f"Pizza 1 is better value ({price_per_area1:.2f} €/m² vs {price_per_area2:.2f} €/m²)")
else:
    print(f"Pizza 2 is better value ({price_per_area2:.2f} €/m² vs {price_per_area1:.2f} €/m²)")
