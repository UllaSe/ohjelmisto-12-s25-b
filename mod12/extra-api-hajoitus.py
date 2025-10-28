import json
import requests


headers = {
    "content-type": "application/json",
    "x-api-key": "reqres-free-v1"
}
payload = json.dumps(
    {
        "username": "käyttäjä",
        "email": "käyttäjäs@käyttäjä",
        "password": "käyttäjä"
    })
requestUrl = "https://reqres.in/api/users"

try:
    # GET
    r = requests.get(requestUrl, headers=headers)
    # POST
    # r = requests.post(requestUrl, data=payload, headers=headers)
    # DELETE
    user_id = 105
    # r = requests.delete(f'https://reqres.in/api/users/{user_id}', headers=headers)
    if  r.status_code==200:
        json_vastaus =  r.json()
        print(json.dumps(json_vastaus, indent=2))

    else:
        raise Exception(f"Non-success status code: {r.status_code}")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")
