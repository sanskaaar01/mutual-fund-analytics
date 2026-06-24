import pandas as pd
import os

# Create processed folder if not exists
os.makedirs("data/processed", exist_ok=True)

# Load data
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date
df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

# Sort by scheme and date
df = df.sort_values(["amfi_code", "date"])

# Convert NAV to numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# Forward fill NAV within each scheme
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Remove rows with invalid dates
df = df.dropna(subset=["date"])

# Save cleaned file
output_file = "data/processed/clean_nav_history.csv"
df.to_csv(output_file, index=False)

print("Cleaned Shape:", df.shape)
print(f"Saved to: {output_file}")