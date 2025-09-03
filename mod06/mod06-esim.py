# Funktio-esimerkkejä
import random

# funktio, joka ei ota parametreja, eikä palauta mitään
def say_hello():
    print("moi")
    print("sinä")

# funktio, joka ottaa vastaan parametreja ja palauttaa arvon
def say_hello_v2(username, age):
    #print("moi")
    #print(username)
    #print(f"Ikäsi: {age}")
    username = username.capitalize() # muuttaa ensimmäisen kirjaimen Isoksi
    return f"Hello {username}!, age: {age}"

#print(say_hello()) # suorittaa funktion ja tulostaa paluuarvon None
#say_hello()
print(say_hello_v2("matti", 5))
nimi = "maija"
return_value = say_hello_v2(nimi, 6)
print(return_value)
print(f"nimi muuttujan arvo: {nimi} ei muutu pääohjelmassa")

## summa-funktio

numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) # built-in sum
print(sum([8, 9, 10]))

## oma toteutus summa-funktiosta (summa + 100)
def my_sum(number_list):
    total = 0
    number_list.append(100) # lisää listaan/summaan aina 100 ylimääräisenä alkiona
    for num in number_list:
        total = total + num
    return total

print(my_sum(numbers))
print(f"Alkuperäisen numbers-muuttujan arvo pääohjelmassa: {numbers}")
print(my_sum([8, 9, 10]))

# listat ja muuttujat
list = [1, 2]
list2 = list # list2 viittaa samaan listaan muistissa
list2.append(3) # koska kyseessä sama lista, myös list1 sisältö muuttuu
print(f"muuttujat list: {list} ja list2: {list2} viittaavat samaan listaan muistissa")
# listasta voidaan luoda myös uusi kopio: list.copy()

## Funktiot ja ohjelman rakenne (alkuperäiset koodit mod4 esimerkeistä)
# komentokehotesovellus ja laskukone
def sum_calculator(num1, num2):
    return num1 + num2

def circumfence(num1, num2):
    return num1 + num2 + num1 + num2

def calculator():
    luku1 = float(input("anna ensimmäinen luku: "))  # esim. "10" -> 10.0
    luku2 = float(input("anna toka luku: "))  # esim. "20" -> 20.0
    total = sum_calculator(luku1, luku2)
    print(f"Yhteenlaskutoimituksen tulos: {total}")
    print(f"Suorakulmion piiri, jossa leveys {luku1} ja korkeus {luku2}"
          f" on: {circumfence(luku1, luku2)}")

def coin_simulator():
    # kolikonheitto n kertaa, kuinka monta kertaa kolikko jäi pystyyn?
    n = 10000
    i = 0
    kolikko_pystyssa_lkm = 0
    while i < n:
        i += 1
        satunnaisluku = random.randint(0, 1000)
        print(f"Arvottu luku: {satunnaisluku}")
        if satunnaisluku < 500:
            print("Kruuna")
        elif satunnaisluku > 500:
            print("Klaava")
        else:  # totetuu muissa tapauksissa, eli jo arvottu luku on tasan 50 (tod.näk: 1/101)
            print("Kolikko jäi pystyyn!")
            kolikko_pystyssa_lkm += 1
    print(f"Kolikko jäi pystyyn {kolikko_pystyssa_lkm} kertaa.")

app_running = True
# "main loop"
while app_running:
    command = input("Komento> ")
    print(f"Komentosi oli: {command}")
    if command == "lopeta":
        app_running = False
    elif command == "laskukone":
        calculator()
    elif command == "kolikkopeli":
        coin_simulator()