CREATE TABLE dim_fund (

amfi_code INTEGER PRIMARY KEY,

scheme_name TEXT,

fund_house TEXT,

category TEXT,

sub_category TEXT,

risk_category TEXT

);

CREATE TABLE dim_date (

date_id INTEGER PRIMARY KEY,

date DATE

);

CREATE TABLE fact_nav (

id INTEGER PRIMARY KEY AUTOINCREMENT,

amfi_code INTEGER,

date_id INTEGER,

nav REAL,

FOREIGN KEY(amfi_code)

REFERENCES dim_fund(amfi_code),

FOREIGN KEY(date_id)

REFERENCES dim_date(date_id)

);

CREATE TABLE fact_transactions (

id INTEGER PRIMARY KEY AUTOINCREMENT,

amfi_code INTEGER,

date_id INTEGER,

amount REAL,

transaction_type TEXT

);

CREATE TABLE fact_performance (

id INTEGER PRIMARY KEY AUTOINCREMENT,

amfi_code INTEGER,

expense_ratio REAL

);

CREATE TABLE fact_aum (

id INTEGER PRIMARY KEY AUTOINCREMENT,

fund_house TEXT,

aum REAL

);