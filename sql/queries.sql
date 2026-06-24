-- 1 Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 3 Average NAV by scheme
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 4 Transaction count by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 5 SIP vs Lumpsum vs Redemption
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 6 Funds with expense ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7 Average transaction amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 8 Top states by investment
SELECT state, SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- 9 Fund count by category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10 Average Sharpe ratio
SELECT AVG(sharpe_ratio)
FROM fact_performance;