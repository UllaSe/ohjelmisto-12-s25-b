
class Koira:
    # konstruktori (rakentaja) -metodi
    def __init__(self, name):
        print(f"uusi koiraolio ({name}) luotu.")
        self.name = name
    # luokan toiminto eli metodi (vrt. funktio)
    def hauku(self, toWhom):
        print(f"{self.name} haukkuu {toWhom}")

koira1 = Koira("Rekku")
koira2 = Koira("Ruffe")
koira1.hauku("Matille")
koira2.hauku("Jussille")

#koira3 = koira1
#print(koira1.name)
#print(koira2.name)
#print(koira3.name)
#koira3.name = "Beethoven"
#koira1.hauku("isännälle")