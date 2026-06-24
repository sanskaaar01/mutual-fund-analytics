from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

files = {
    "dim_fund":
        "data/raw/01_fund_master.csv",

    "fact_nav":
        "data/processed/clean_nav_history.csv",

    "fact_transactions":
        "data/processed/clean_transactions.csv",

    "fact_performance":
        "data/processed/clean_scheme_performance.csv",

    "fact_aum":
        "data/raw/03_aum_by_fund_house.csv"
}

for table, file in files.items():

    df = pd.read_csv(file)

    df.to_sql(
        table,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table}: {len(df)} rows loaded"
    )

print("\nDatabase Created")