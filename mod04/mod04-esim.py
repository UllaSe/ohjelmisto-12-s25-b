# while-toistolause eli silmukka eli luuppi
import random

suorita_silmukka = True

while suorita_silmukka:
    suorita_silmukka = False
    print("totta")
    print("on vain kerran")
print("silmukan suoritus loppui")

# iteraattori ja while
toistojen_lkm = 10
i = 0
while i < toistojen_lkm:
    print(f"iteroiva silmukka, i:n arvo: {i}")
    i = i + 1
    # lyhyt muoto: i += 1

print(f"i:n arvo lopuksi: {i}")

# komentokehotesovellus ja laskukone
app_running = True
# "main loop"
while app_running:
    command = input("Komento> ")
    print(f"Komentosi oli: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "laskukone":
        luku1 = float(input("anna ensimmäinen luku: "))  # esim. "10" -> 10.0
        luku2 = float(input("anna toka luku: "))  # esim. "20" -> 20.0
        tulos_yhteenlasku = luku1 + luku2 # liukuluvuilla
        print("Yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))

# kolikonheitto n kertaa, kuinka monta kertaa kolikko jäi pystyyn?
n = 10000
i = 0
kolikko_pystyssa_lkm = 0
while i < n:
    i += 1
    satunnaisluku = random.randint(0,1000)
    print(f"Arvottu luku: {satunnaisluku}")
    if satunnaisluku < 500:
        print("Kruuna")
    elif satunnaisluku > 500:
        print("Klaava")
    else: # totetuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/101)
        print("Kolikko jäi pystyyn!")
        kolikko_pystyssa_lkm += 1
print(f"Kolikko jäi pystyyn {kolikko_pystyssa_lkm} kertaa.")