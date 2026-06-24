-- 1. Top 5 funds by AUM

SELECT fund_house,
aum_crore

FROM fact_aum

ORDER BY aum_crore DESC

LIMIT 5;



-- 2. Average NAV per month

SELECT

strftime('%Y-%m',date)

AS month,

AVG(nav)

AS avg_nav

FROM fact_nav

GROUP BY month;



-- 3. SIP transactions by year

SELECT

strftime('%Y',transaction_date)

AS year,

COUNT(*)

AS sip_count

FROM fact_transactions

WHERE transaction_type='SIP'

GROUP BY year;



-- 4. Transactions by state

SELECT

state,

COUNT(*)

AS transactions

FROM fact_transactions

GROUP BY state;



-- 5. Funds with expense ratio below 1%

SELECT

scheme_name,

expense_ratio_pct

FROM fact_performance

WHERE expense_ratio_pct <1;



-- 6. Top 5 risk categories

SELECT

risk_category,

COUNT(*)

FROM dim_fund

GROUP BY risk_category;



-- 7. Total AUM by fund house

SELECT

fund_house,

SUM(aum_crore)

FROM fact_aum

GROUP BY fund_house;



-- 8. Average return (1 year)

SELECT

AVG(return_1yr_pct)

FROM fact_performance;



-- 9. Transactions by payment mode

SELECT

payment_mode,

COUNT(*)

FROM fact_transactions

GROUP BY payment_mode;



-- 10. Top categories

SELECT

category,

COUNT(*)

FROM dim_fund

GROUP BY category;