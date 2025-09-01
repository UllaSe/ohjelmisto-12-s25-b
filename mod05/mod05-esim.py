nimi = 'Ulla'
nimi2 = 'Matti'
num1 = 45
num2 = 56

print(f'Hei {nimi} ikäsi on {num1}')

# tyhjä lista
lista = []

# lista voi sisältää muuttujia, numeroita, merkkijonoja jne.
nimet = ['Anna', 'Liisa', nimi, nimi2, 'Toni', 'Ilkka']
print(nimet)

# lista voi sisältää toisia listoja
ikälista = [45, 67, 34, [98, 4, 17]]
print(ikälista)

# listan pituus voidaan takistaa len(funktiolla)
print(len(nimet))
# tehkää oma lista ja printatkaa vielä kerran sen pituus


print('-----------------------')
print('VIIPAILOINTI')
print('-----------------------')
# Listasta voidaan hakea tietoa alkion indeksin avulla
# TAI viipaloinnilla

# alkioon viitataan indeksinumerolla, alkaen numerosta 0
print(f'Hei {nimet[0]} ja terve myös {nimet[4]}')

print(ikälista[3][1])
print(len(ikälista[3]))

print('-----------------------')
# tapoja viitata listan alkioihin
nimet2 = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Anna", "Ulla", "Pasi"]
print(nimet2[3])    #olga
print(nimet2[1])    #ahmed
print(nimet2[1:5])  #(alkupiste mukaan lukien) ja indeksiin 3 päättyen (päätepiste pois lukien)
print(nimet2[-1])
print(nimet2[2:])
print(nimet2[1:-1])
print(nimet2[1:-1:2])
print('-----------------------')

# uusi_lista = vanha_lista[alku:loppu:askel]
uusi_lista = nimet2[2:4]
print(nimet2)
print(uusi_lista)

print('-----------------------')

# lista jossa 5 kaupunkia
# tulosta niistä 3 ensimmäistä ja viimeinen
kaupungit = ["Helsinki", "Tampere", "Turku", "Oulu", "Jyväskylä"]
print(kaupungit[:3])
print(kaupungit[-1])

# viittaus listan ulkopuolelle aiheuttaa virheen!!!
#print(kaupungit[7])

kaupungit.append('Uusi kaupunki')
print(kaupungit)
# kaupungit.remove('Iisalmi') -> virhe koska kaupunkia ei löydy

if "Tampere" in kaupungit:
    print(f'Tampere löytyi ja poistetaan listasta!!!')
    # poistetaan kaupunki
    kaupungit.remove('Tampere')
    print(kaupungit)

# lisätään Tampere ensimmäiseksi
kaupungit.insert(0, 'Tampere')
print(kaupungit)

# tutkitaan monesko indeksi
monesko = kaupungit.index('Oulu')
print(monesko)

lisää_kaupunkeja = ['Sodankylä', 'Sipöö', 'Kotka']
kaupungit.extend(lisää_kaupunkeja)
print(kaupungit)

# muokataan olemassa olevaa alkiota indeksin avulla
kaupungit[7] = 'Sipoo'
print(kaupungit)

hedelmiä = ['greippi', 'appelsiini', 'Appelsiini', 'banaani']
numerolista = [1000, 5, 666, 3, 8]

hedelmiä.sort()
print(hedelmiä)

numerolista.sort(reverse=True)
print(numerolista)

tottavaiei = True # python on dynaamisesti tyypitetty, nyt boolean
tottavaiei = 'True' # nyt string
print(type(tottavaiei))

viikonpaivat = ['Maanantai', 'Tiistai']
print(viikonpaivat)

print('-----------------------')
print('Muutamia hyödyllisia funktiota tulevaisuutta varte')
print('-----------------------')

# listoille toimii mm. tämänlaiset funktiot
# len, sum, min, max, count
luvut = [2,4,6,5,2,7,2,7]
print(len(luvut)) # pituus
print(sum(luvut)) # lukujen summa
print(min(luvut)) # pienin numero
print(max(luvut)) # isoin numeroa
print(luvut.count(2)) # kuinka monta lukua 2 listassa on

print('-----------------------')
print('Miten käydään lista läpi iteroimalla')
print('-----------------------')

luvut[2]

# luvut = [2,4,6,5,2,7,2,7]

i = 0
while i < len(luvut):
    # print(i)
    print(luvut[i])
    # i = i + 1
    i += 1

print('-----------------------')
# käydä listan läpi alkio alkiolta


for kirjain in 'abcdefg':
    print(kirjain)

print('-----------------------')

for alkio in [1, 2, 3, 4, 5, 6]:
    print(alkio)

print('-----------------------')

for luku in luvut:
    print(luku)

print('-----------------------')

# tässä tapauksessa kaupunki on kierrosmuuttuja
for kaupunki in kaupungit:
    print(kaupunki)

print('-----------------------')

for numero in range(5):
    print(numero)

for n in range(4,80, 2):
    print(n)

print('-----------------------')
print('Nurinpäin')

for n in range(50, 0, -2):
    print(n)

print('-----------------------')

#luvut = [2,4,6,5,2,7,2,7]
luvut_listan_pituus = len(luvut)
for n in range(luvut_listan_pituus):
    # print(n) -> tämä on iteraattori
    print(luvut[n])

print('-----------------------')
# printataan vain 3
for n in range(3):
    print(kaupungit[n])
















