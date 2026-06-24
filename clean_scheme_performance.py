import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Flag anomalies
anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print(
    "Expense Ratio Anomalies:",
    len(anomalies)
)

# Save anomaly report
anomalies.to_csv(
    "data/processed/performance_anomalies.csv",
    index=False
)

# Remove duplicates
df = df.drop_duplicates()

output_file = (
    "data/processed/clean_scheme_performance.csv"
)

df.to_csv(
    output_file,
    index=False
)

print("Cleaned Shape:", df.shape)
print("Saved:", output_file)