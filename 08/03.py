import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
         host='',
         port= ,
         database='',
         user='',
         password='',
         autocommit=
         )

def airport_location(icao):
    sql = f"select latitude_deg, longitude_deg from airport where ident = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchall()
    return result

airport1 = input("icao of airport 1? ")
airport2 = input("icao of airport 2? ")
print(f"{airport1} is at {airport_location(airport1)}")
print(f"{airport2} is at {airport_location(airport2)}")
print(f"The distance between {airport1} and {airport2} is {distance.distance(airport_location(airport1), airport_location(airport2)).km:.2f}km)")