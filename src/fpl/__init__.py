import requests

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)

data = response.json()

print(data.keys())