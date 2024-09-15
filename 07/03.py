def add_airport():
    icao = input("enter the ICAO code\n")
    name = input("name of the airport\n")
    airports[icao] = name
    print(f"Added {icao} as {name}")

def fetch_airport():
    airport = input("enter the ICAO code of the airport\n")
    if airport in airports:
        print(f"{airport} is {airports[airport]}")
    else:
        print("airport not in dictionary")

airports = {}

while True:
    action = input("What do you want to do? Options: enter, fetch, quit\n")

    if action == "enter":
        add_airport()
    if action == "fetch":
        fetch_airport()
    if action == "quit":
        break
    if action == "secret fourth option":
        print("yay! (●'◡'●)")
