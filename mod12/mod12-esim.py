import requests
import json

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyyntö).json()
# tämä on lähinnä koko vastauksen muotoilua varten
print(json.dumps(vastaus, indent=2))

sanakirja = vastaus[0]
print(sanakirja['show']['genres'][0])

for a in vastaus:
    print(a["show"]["name"])

# lista, käytetään index
# lista[0][0]

# sanakirja, käytetään avain
# sanakirja['show']['name']