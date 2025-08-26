# valintarakenne-esimerkkejä (mod3)
import random

#onko_totta = False
#onko_totta = 3 == 3

satunnaisluku = random.randint(0,100)
#print(f"Arvottu luku: {satunnaisluku}")

# kolikonheittosimulaattori
if satunnaisluku < 50:
    print("Kruuna")
    print("kuulu samaan koodilohkoon")
elif satunnaisluku > 50:
    print("Klaava")
else: # totetuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/101)
    print("Kolikko jäi pystyyn!")

print("Ohjelman suoritus if-lauseen jälkeen jatkuu tästä.")

# dummy-kirjautuminen
oikea_salasana = "salakala"
tunnus = "matti"
input_tunnus = input("Käyttäjätunnus: ")
input_salasana = input("Anna salasana: ")

# Testataan, että kumpikin ehto on totta
if input_salasana == oikea_salasana and input_tunnus == tunnus:
    print("Tervetuloa!")
    kehote = input("Mitäs haluat tehdä? ")
    if kehote == "tervehtiä":
        print("No morjes!")
    else:
        print("en ymmärtänyt kehotetta")
else:
    print("Väärä salasana")

print("Ohjelma suljettu. Heippa!")
