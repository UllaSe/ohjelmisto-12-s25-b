# 20.8. tuntiesimerkkejä

"""
monirivinen kommentti (merkkijono, string)
voidaan myös sijoittaa muuttujaan
"""
import math
import random

nimi = input("Anna nimesi: ") # palauttaa merkkijonon (str)
ika = 20 # kokonaisluku (int)
ika_ensi_vuonna = ika + 1 # int
str_ika_ensi_vuonna = str(ika_ensi_vuonna) # -> "21"

tervehdys = "Moi " + nimi + " " + str_ika_ensi_vuonna

print(tervehdys)

# Simppleli laskukone

# luetaan käyttäjältä kaksi luku (str), jotka muunnetaan samantien
# liukuluvuiksi ja sijoitetaan muuttujiin
luku1 = float(input("anna ensimmäinen luku: ")) # esim. "10" -> 10.0
luku2 = float(input("anna toka luku: ")) # esim. "20" -> 20.0

# lasketaan tulos numeerisilla arvoilla
# tulos = int(luku1) + int(luku2) # kokonaisluvuilla
tulos_yhteenlasku = luku1 + luku2 # liukuluvuilla
tulos_vahennyslasku = luku1 - luku2
tulos_jakolasku = luku1 / luku2
kokonaisosa = luku1 // luku2
jakojaannos = luku1 % luku2
tulos_kertolasku = luku1 * luku2
tulos_potenssiin_korotus = luku1 ** luku2

#tulos = 1+2 # 3 (kovakoodattu arvo test)
print("Yhteenlaskutoimituksen tulos: " + str(tulos_yhteenlasku))
print("Vähennyslaskun tulos: " + str(tulos_vahennyslasku))
# tulosteen muotoilu f-stringillä (kannattaa)
print(f"Jakolaskun tulos: {tulos_jakolasku:.2f}, jossa kokonaisosa on "
      f"{kokonaisosa}, desimaaliosa {tulos_jakolasku - kokonaisosa} ja "
      f"jakojaannos {jakojaannos}")
# TODO: tulosta loput tulokset

# ympyrän ala: pi * r^2: 3.14159 * r^2
# piin arvo math-kirjastosta (import-lause tiedoston alussa tarvitaan)
print(f"pii: {math.pi:.8f}")

# satunnaisluvun generointi väliltä 1-6
print(random.randint(1, 6))
