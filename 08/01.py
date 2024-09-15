import mysql.connector

connection = mysql.connector.connect(
         host='',
         port= ,
         database='',
         user='',
         password='',
         autocommit=
         )

def get_airport_from_ident(icao):
    sql = f"select name, municipality, iso_country from airport where ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result


while True:
    code = input("enter icao code, or empty string to quit\n")
    if code == "":
        break
    else:
        airport = get_airport_from_ident(code)
        if airport is not None:
            print(f"{airport['name']} is in {airport['municipality']}, {airport['iso_country']}")
        else:
            print("invalid input")