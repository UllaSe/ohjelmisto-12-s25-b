import json
import requests

city_name = input('Anna kaupungin nimi: ')
API_key = "906fb34bfe2c0b225f7bb95667a12ee1"
# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
lang = 'fi'
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"


try:
    vastaus = requests.get(pyyntö)
    print('Status code', vastaus.status_code)
    if vastaus.status_code==200:
        data = vastaus.json()
        print(json.dumps(data, indent=2))
        print(f'Sää kohteessa {city_name} on {data['weather'][0]['description']}')

except requests.exceptions.RequestException as e:
    print(e)
    print ("Hakua ei voitu suorittaa.")