import requests
import pandas as pd
import os

# Scheme names and IDs

scheme_ids = {
    "hdfc_top_100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

# Create folder if it doesn't exist

os.makedirs("data/raw", exist_ok=True)

# Fetch each scheme

for scheme_name, scheme_id in scheme_ids.items():

    url = f"https://api.mfapi.in/mf/{scheme_id}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{scheme_name}_nav.csv"

    df.to_csv(file_path, index=False)

    print(f"✅ Saved {scheme_name}")
    
print("\nAll NAV files downloaded successfully.")