class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

# luodaan pysyvä assosiaatiosuhden Hoitola ja Koira-luokkien välillä
# Koirat tallennetaan luokan ominaisuutena olevaan koiralistaan

class Hoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat = []

    # metodi, jonka parametrina annetaan viittaus Koira olioon
    # assosiaatiotsuhde on voimassa vain metodikutsun ajan
    def koira_sisään(self, koira):
        #print(koira)
        print(f'Lisätään koira {koira.nimi} sisään hoitolaan')
        self.koirat.append(koira)
        # kutsutaan olion omia metodeja
        self.printtaa_koirat()
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f'👋🏻 heippa {koira.nimi} ja hyvää kotimatkaa!!')
        return

    def printtaa_koirat(self):
        print(f'Hoitolassa {self.nimi} on seuraavat koirat:')
        for koira in self.koirat:
            print(koira.nimi)

    def tervehdi_koiria(self, kerrat):
        print('Tervehditään koiria ja jokainen koira haukkuu: ')
        for koira in self.koirat:
            koira.hauku(kerrat)

class Yritys:
    def __init__(self, nimi, osoite):
        self.nimi = nimi
        self.osoite = osoite
        self.hoitolat = []

    def lisaa_hoitolat(self, hoitola):
        self.hoitolat.append(hoitola)

    def tulosta_hoitola(self):
        for h in self.hoitolat:
            print(h.nimi)

    def anna_joululahja(self):
        print('Yritys antaa joululahjan jokaiselle koiralle 🐶')

        # Jokainen koira jokaisessa hoitolassa haukahtaa kerran
        # iteroidaan kaikki läpi
        '''
        for h in self.hoitolat:
            print(f'Annetaan lahjoja {h.nimi} koirille:')
            for koira in h.koirat:
                print(f'{koira.nimi} saa joululahjaksi luun!')
                koira.hauku(1)
        '''
        # käytetään metodeja
        for hoitola in self.hoitolat:
            print('Yritys antaa toisen luun')
            hoitola.tervehdi_koiria(1)



koira1 = Koira('Muro', 2018, 'WOOOOOOOFFF')
koira2 = Koira('Lissu', 2020, 'YipYip')
koira3 = Koira('Musti', 2022, 'Hauhau')
koira4 = Koira('Fifi', 2025, 'WUF WUF')
print(koira1.nimi)
koira1.hauku(3)

onnentassu = Hoitola('Onnentassu')
onnentassu.koira_sisään(koira1)
onnentassu.koira_sisään(koira2)
# onnentassu.printtaa_koirat()

pikkukoirat = Hoitola('Pikkukoirat')
pikkukoirat.koira_sisään(koira3)
pikkukoirat.koira_sisään(koira4)
pikkukoirat.printtaa_koirat()

# tervehdi koiria
onnentassu.tervehdi_koiria(3)

#poistakoira
onnentassu.koira_ulos(koira1)

# lisää yritys
yritys = Yritys('Musti & Mirri', 'Osoite 1234')
yritys.lisaa_hoitolat(onnentassu)
yritys.lisaa_hoitolat(pikkukoirat)

yritys.tulosta_hoitola()
yritys.anna_joululahja()




