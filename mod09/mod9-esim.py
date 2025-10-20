
class Koira:
    count = 0
    # konstruktori (rakentaja) -metodi ajetaan kun luokasta luodaan olio
    def __init__(self, name, weight):
        print(f"uusi koiraolio ({name}) luotu.")
        # nimi tallennetaan olion ominaisuudeksi self-viittauksen avulla
        self.name = name
        self.weight = weight
        Koira.count = Koira.count + 1
    # luokan toiminto eli metodi (vrt. funktio)
    def hauku(self, toWhom, times=1):
        print(f"{self.name} haukkuu {toWhom}")
        for i in range(times):
            if self.weight < 10:
                print("Wufwuf")
            else:
                print("Hauhau")

koira1 = Koira("Rekku", 4)
koira2 = Koira("Ruffe", 28)
koira1.hauku("Matille", 2)
koira2.hauku("Jussille")
print(f"Koiraolioita on luotu yhteensä {Koira.count} kpl.")

# koira3 muuttuja viittaa samaan olioon kuin koira1
koira3 = koira1

koira2 = koira1

koira2.hauku("Matti")
#print(koira1.name)
#print(koira2.name)
#print(koira3.name)
#koira3.name = "Beethoven"
#koira1.hauku("isännälle")