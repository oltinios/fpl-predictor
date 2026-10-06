import requests
import json

def fetch_data(url):
    response = requests.get(url)

    data = response.json()

    return data

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

data = fetch_data(url)

with open("data/raw/bootstrap.json", "w") as file:
    json.dump(data, file, indent=2)