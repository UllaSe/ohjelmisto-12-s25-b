# Mod 9 tehtävät johdantoa
class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        #TODO: anna huippunopeus ja rekkari alustajan parametreina
        self.top_speed = 100
        self.register_number = "abc-123"
    def accelerate(self):
        #TODO: anna nopeuden muutos parametrina ja huomioi huippunopeus
        # auton nopeus ei saa mennä negatiiviseksi
        self.speed += 1

# luodaan auto-olioita suoraan listan alkioiksi
#cars = [Car(), Car()]
# tai toistorakenteella
cars = []
for i in range(9):
    cars.append(Car())

cars[0].accelerate()
cars[0].accelerate()
print(f"Auto 1 nopeus: {cars[0].speed}, auto 2: {cars[1].speed}")

# tulostetaan kaikkien autojen nopeudet
for car in cars:
    print(f"Auton {car.register_number} nopeus: {car.speed}")