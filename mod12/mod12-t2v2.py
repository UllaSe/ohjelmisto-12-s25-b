import json
import requests

city_name = input('Anna kaupungin nimi: ')
API_key = "906fb34bfe2c0b225f7bb95667a12ee1"
# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
lang = 'fi'
lat = ''
lon = ''

pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}"
try:
    vastaus = requests.get(pyyntö)
    print('Status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        eka = data[0]
        print(eka)
        lat, lon = eka['lat'], eka['lon']
        print(f'Kaupunkin {city_name} leveysaste on {lat}, pituusaste on {lon}')
except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")


# tämä tehdään kun geocoding api palauttaa ensin lat ja lon

pyyntö2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
try:
    vastaus = requests.get(pyyntö2)
    print('Status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))

except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")

# TODO: hakekaa oikea tieto ja printatkaa kyseisen lokaation sää siistissä muodossa käyttäjälle

