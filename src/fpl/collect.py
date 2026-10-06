import json
import requests
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    return data

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

data = fetch_data(url)

output_file = PROJECT_ROOT / "data" / "raw" / "bootstrap.json"

with open(output_file, "w") as file:
    json.dump(data, file, indent=2)