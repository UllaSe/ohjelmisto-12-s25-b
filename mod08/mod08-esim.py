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

# funktio, joka hakee maan se koodin perusteella
def get_country_name_by_code(code):
    sql = f"SELECT name FROM country WHERE iso_country = '{code}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    # jos tulosjoukko on tyhjä
    if result:  # sama kuin result != None:
        return result[0]
    return "Ei löydy"

# "käyttöliittymä maahakusovellukselle"
country_code = input("Anna maakoodi: ")
country = get_country_name_by_code(country_code)
print(f"Maakoodi: {country_code}, hakutulos: {country}")

# SQL insert esimerkki, uuden maan lisäys country-tauluun
def add_country(code, name):
    sql = f"INSERT INTO country (iso_country, name) VALUES ('{code}', '{name}')"
    cursor = connection.cursor()
    # HUOM: kaatuu sql-virheeseen, jos yritetään syöttää samaa pääavainarvoa uudelleen
    # Virheenkäsittelyä käsitellään myöhemmin
    cursor.execute(sql)
    #print(cursor)
#add_country('xyz', 'testcountry')