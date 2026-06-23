import pandas as pd

master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(master["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = master_codes - nav_codes

print("Total schemes in fund master:", len(master_codes))
print("Total schemes in NAV history:", len(nav_codes))
print("Missing AMFI codes:", len(missing))

if len(missing) > 0:
    print("\nMissing Codes:")
    print(missing)
else:
    print("\nAll AMFI codes found successfully.")