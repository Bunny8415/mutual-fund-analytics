import requests
import pandas as pd
import os

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["data"])

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/hdfc_nav.csv", index=False)

print("CSV saved successfully")