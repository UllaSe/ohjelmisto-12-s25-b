import mysql.connector

# otetaan tietokantayhteys
connection = mysql.connector.connect(
    port=3306, # oletusarvo, ei pakollinen parametri
    host="localhost", # oletusarvon, ei pakollinen
    database="flight_game2",
    user="username",
    password="password",
    autocommit=True
)
#print(connection)
# luodaan osoitin ja sijoitetaan viittaus siihen muuttujaan
cursor = connection.cursor()
# käytetään osoitinta tietokantahakuun
cursor.execute("SELECT name, iso_country FROM country")
# haetaan tulosjoukosta rivi kerrallaan
result = cursor.fetchone() # palauttaa rivin pyydetyt sarakkeen monikkona
print(result)
result = cursor.fetchone()
print(result)
# haetaan seuraavat 3 riviä tulosjoukosta, palauttaa "rivimonikot" listana
result = cursor.fetchmany(3)
print(result)
# yleisin tapa: haetaan kaikki (loput) tulokset
result = cursor.fetchall()
print(result)
print(f"result listan pituus {len(result)}")
# tulostetaan ensimmäisen rivin maakoodi
print(result[0][1])

# tulostetaan tulosjoukko muotoiltuna
for country in result:
    print(f"Maan {country[0]} maakoodi on: {country[1]}")