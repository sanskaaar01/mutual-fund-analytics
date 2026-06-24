import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Fix date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

mapping = {
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Amount > 0
df = df[df["amount_inr"] > 0]

# Standardize KYC values
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid dates
df = df.dropna(subset=["transaction_date"])

output_file = "data/processed/clean_transactions.csv"

df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print("Saved:", output_file)