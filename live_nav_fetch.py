import requests
import pandas as pd
import os

os.makedirs("data/raw/live_nav", exist_ok=True)

scheme_codes = {
    "sbi_small_cap": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/live_nav/{name}.csv",
        index=False
    )

    print(f"Saved {name}")