import json
import requests
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def fetch_data(url, output_file):
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    with open(output_file, "w") as file:
        json.dump(data, file, indent=2)

    return data

bootstrap_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
bootstrap_file = PROJECT_ROOT / "data" / "raw" / "bootstrap.json"

bootstrap_data = fetch_data(
    bootstrap_url,
    bootstrap_file
)

fixtures_url = "https://fantasy.premierleague.com/api/fixtures/"
fixtures_file = PROJECT_ROOT / "data" / "raw" / "fixtures.json"

fixtures_data = fetch_data(
    fixtures_url,
    fixtures_file
)