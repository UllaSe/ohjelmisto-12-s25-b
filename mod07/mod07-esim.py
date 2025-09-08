import random

# MONIKKO
###############

# monikko eli (tuple) on "kuin lista jota ei voi muokata"

lista = [1 ,2, 3, 4, 5, 6]
print(lista)

monikko = (1, 2, 3, 4, 5, 6)
print(monikko)

# monikon voi luoda ilman kaarisulkeita
monikko2 = 1, 2, 3, 4, 5, 6
print(monikko2)

# monikko voi sisältää erilaista tietoa
monikko3 = (1, 2, 'Ulla', (3 ,4), 88)
print(monikko3)

#luetaan listan sekä monikon eka alkio
print(lista[0])
print(monikko[0])

# Toisin kuin lista, monikko on kuitenkin muuttumaton: siihen ei voi lisätä alkioita eikä siitä voi poistaa alkioita monikon luonnin jälkeen.
lista[0] = 0
lista.append(7)
print('Muokattu lista', lista)

# tämä ei toimi monikolla, on muokkaamaton
# monikko[0] = 0

# monikosta voi hakea indeksin avulla alkion arvon
luku = monikko[3]
print('Hain tämän monikosta:', luku)

#Monikkoa on tarkoituksenmukaista käyttää tilanteissa, joissa alkioiden jono on luonteeltaan staattinen: tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana.

'''
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")
'''

# Monikon läpikäynti kuten listan
sanat = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')

for sana in sanat:
    print(sana)
    if sana == 'kolmas':
        print('Sana KOLMAS löytyi!!!')

if 'viides' in sanat:
    print('Sana VIIDES löytyi!!!!')

# Monikon arvojen purku muuttujiin

hedelmät = ('Lime', 'Sitruuna', 'Ananas')
print(hedelmät)
# (eka, toka, kolmas) = ('Lime', 'Sitruuna', 'Ananas')
(eka, toka, kolmas)  = hedelmät
print('Monikko purettu muuttujiin, tässä eka', eka)

# Monikon voi antaa funktiolle parametrina

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)

tulosta_monikko(hedelmät)

# Monikko funktion paluuarvona

# perinteisesti
def heitä():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    print(f'Nopista tuli {eka} ja {toka}')
heitä()

# yksinkertaistetaan random
def heitä2():
    # tässä luodaan tuple eli monikko joka puretaan muuttujiin
    # eka, toka = (random.randint(1, 6), random.randint(1, 6))
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f'Nopista tuli {eka} ja {toka}')
heitä2()

# monikko myös paluuarvona
def heitä3():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

noppa1, noppa2  = heitä3()
print('Funktiosta heitä3 palautui arvot:', noppa1, noppa2)

print('--------------------------------')
print('JOUKKO\n')

# joukko eli set {}

# Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä
# alkioihin ei voi myöskään viitata indeksillä.
# toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen

# joukko merkataan aaltosulkeilla
joukko = {1,2,3,4,5,6}
print(joukko)

llista = [1,2,3,4,5,6,6,] #ok
mmonikko = (1,2,3,4,5,6,6) #ok
print(f'Numero 6 EI voi esiintyä joukossa useasti')
jjoukko = {1,2,3,4,5,6,6}
print(jjoukko)

# yllä oleva ei sinänsä tuota virhettä, kuten ei add-metodi
jjoukko.add(6) # tämä ei aiheuta virhettä, mutta ei lisää uutta numeroa 6
jjoukko.add(7) # toimii
print(jjoukko)
jjoukko.remove(1)
print(jjoukko)

pelit = {"Monopoli", "Shakki", "Cluedo", "Muuttuva labyrintti", "Hotel"}
print(pelit)
pelit.add("Cluedo")
print(pelit)

# alkioiden iteroiminen läpi for/in rakenteella
# indeksiin ei voi tosiaan tässä viitata
for p in pelit:
    print(p)

if "Cluedo" in pelit:
    print(f'Cluedo löytyi listasta 😀 ')

print('-----------\n')

# tyhjän listan luomine
autolista = []
autolista.append('Audi')
print(autolista)
print(type(autolista))

# tyhjä joukko luodaan edellä esitetystä poiketen set-funtion avulla
autojoukko = set()
autojoukko.add('Mersu')
print(autojoukko)
print(type(autojoukko))

# jos yritätä luoda tyhjää joukkoa {} sulkeilla, tästä tuleekin sanakitja
autosanakirja = {}
print(type(autosanakirja))

print('SANAKIRJA\n')

# Sanakirja (dictionary) on Pythonin käytetyimpiä tietorakenteita.
# Sanakirjaan voidaan tallentaa avain-arvopareja.

# kun sanakirja alustetaan, annetaan avain-arvopari seuraavasti: AVAIN : ARVO
# peräkkäiset avain-arvoparit erotellaan pilkulla

oppilaat = {
    'Aapeli': 25,
    'Bertta': 56,
    'Cecilia': 53,
    'Daniel': 23,
    'Emma': 25
}
print(oppilaat)

# mitä ovat tietueet / items
print(oppilaat.items())

# mitä ovat avaimet sanakirjassa
print(oppilaat.keys())

# mitä ovat arvot / values sanakirjassa
print(oppilaat.values())

# käydään läpi sanakirja nyt for / in rakenteella
# kierrosmuuttuja eli tässä tapauksessa o saa arvokseen
# kunkin sanakirjassa esiintyvän AVAIMEN

oppilaat = {
    'Aapeli': 25,
    'Bertta': 56,
    'Cecilia': 53,
    'Daniel': 23,
    'Emma': 25
}

for o in oppilaat:
    print(o)

avain = 'Aapeli'
# oppilaat[avain]
print('Etsitään avaimella Aapeli hänen ikä', oppilaat[avain])
print(f'Danielin ikä: {oppilaat['Daniel']}')

for o in oppilaat:
    print(f'Oppilaan nimi on {o} ja IKÄ on {oppilaat[o]}')

# hae haluttu ikä if / in rakennetta käyttäen
# 1. pyydä käyttäjältä nimi ja haetaan se sanakirjasta

nimi = input('Anna nimi jota etsin sanakirjasta: ')
if nimi in oppilaat:
    ikä = oppilaat[nimi] # haetaan avaimella arvo
    print(f'Nimi {nimi} löytyi!!!!')
    print(f'Hänen ikä on {ikä}')
else:
    print(f'Nimeä {nimi} ei löydy sanakirjasta')


# extra: moniulotteinen sanakirja, tätä tulet tarvitsemaan seuraavilla tunneila
yhteystiedot = {
    'Aapeli': {
        'puh': '0503546585',
        'osoite': 'Linnuntie 5'
    },
    'Bertta': {
        'puh': '0406797466',
        'osoite': 'Rapakuja 7'
    },
    'Cecilia': {
        'puh': '0406797466',
        'osoite': 'Tullihaukankuja 8'
    }
}
print(f'Aapelin puhelinnumero: {yhteystiedot['Aapeli']['puh']}')





