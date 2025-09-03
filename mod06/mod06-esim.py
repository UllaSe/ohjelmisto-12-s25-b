# Funktio-esimerkkejä

# funktio, joka ei ota parametreja, eikä palauta mitään
def say_hello():
    print("moi")
    print("sinä")

# funktio, joka ottaa vastaan parametreja ja palauttaa arvon
def say_hello_v2(username, age):
    #print("moi")
    #print(username)
    #print(f"Ikäsi: {age}")
    return f"Hello {username}!, age: {age}"

#print(say_hello()) # suorittaa funktion ja tulostaa paluuarvon None
#say_hello()
print(say_hello_v2("matti", 5))
return_value = say_hello_v2("maija", 6)
print(return_value)

## summa-funktio

numbers = [1, 2, 3, 4, 5]
print(sum(numbers)) # built-in sum
print(sum([8, 9, 10]))

## oma toteutus
def my_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(my_sum(numbers))
print(my_sum([8, 9, 10]))