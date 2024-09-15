import mysql.connector

connection = mysql.connector.connect(
         host='',
         port= ,
         database='',
         user='',
         password='',
         autocommit=
         )

def get_airports_in_country(icao):
    sql = f"select name, type from airport where iso_country = %s order by type"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()
    return result


while True:
    code = input("enter country code, or an empty string to quit\n")
    if code == "":
        break
    else:
        airport = get_airports_in_country(code)
        if airport is not None:
            for n in airport:
                print(f"{n[0]} is a {n[1]} in {code}")
        else:
            print("invalid input")