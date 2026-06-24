# Data Dictionary

## dim_fund

| Column       | Type    | Description                   |
| ------------ | ------- | ----------------------------- |
| amfi_code    | Integer | Unique AMFI scheme identifier |
| fund_house   | Text    | Mutual fund company           |
| scheme_name  | Text    | Name of scheme                |
| category     | Text    | Fund category                 |
| sub_category | Text    | Fund sub-category             |

## fact_nav

| Column    | Type    | Description       |
| --------- | ------- | ----------------- |
| amfi_code | Integer | Scheme identifier |
| date      | Date    | NAV date          |
| nav       | Real    | Net Asset Value   |

## fact_transactions

| Column           | Type    | Description            |
| ---------------- | ------- | ---------------------- |
| investor_id      | Text    | Investor identifier    |
| transaction_date | Date    | Transaction date       |
| amfi_code        | Integer | Scheme code            |
| transaction_type | Text    | SIP/Lumpsum/Redemption |
| amount_inr       | Real    | Transaction amount     |

## fact_performance

| Column         | Type | Description                  |
| -------------- | ---- | ---------------------------- |
| return_1yr_pct | Real | 1-year return                |
| return_3yr_pct | Real | 3-year return                |
| sharpe_ratio   | Real | Risk-adjusted return         |
| alpha          | Real | Excess return over benchmark |

## fact_aum

| Column     | Type | Description              |
| ---------- | ---- | ------------------------ |
| fund_house | Text | Asset management company |
| aum_crore  | Real | Assets under management  |
