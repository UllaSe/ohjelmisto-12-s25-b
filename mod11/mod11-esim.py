class Elain:
    def __init__(self, nimi, syntymävuosi):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi

    def tulosta_tiedot(self):
        print(f"{self.nimi}, syntymävuosi: {self.syntymävuosi}")

    def puhu(self, kerrat, ääni="---"):
        for i in range(kerrat):
            print(ääni)


class Koira(Elain):
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.haukahdus = haukahdus
        super().__init__(nimi, syntymävuosi)

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
    # ylikirjoitetaan elaimen puhu()-metodi ja kutsutaan sieltä luoka omaa metodia
    def puhu(self, kerrat, ääni="---"):
        self.hauku(kerrat)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"{self.nimi} on koira")


class Kissa(Elain):
    def __init__(self, nimi, vuosi):
        super().__init__(nimi, vuosi)

    def puhu(self, kerrat, ääni="---"):
        super().puhu(kerrat, "Miumiu")


elaimet = []
elaimet.append(Koira("Ruffe", 2020))
elaimet.append(Kissa("Miuku", 2018))
elaimet.append(Elain("Tipu", 2024))


for elain in elaimet:
    elain.tulosta_tiedot()
    elain.puhu(2)
