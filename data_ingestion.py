import pandas as pd
import os

folder_path = "data/raw"

files = os.listdir(folder_path)

for file in files:
    try:
        df = pd.read_csv(os.path.join(folder_path, file))

        print(f"\nFile: {file}")
        print("Shape:", df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("=" * 60)

    except Exception as e:
        print(f"Error loading {file}: {e}")

# outside loop and outside except
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

# Load NAV history

nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Create sets

fund_codes = set(fund_master["amfi_code"])

nav_codes = set(nav_history["amfi_code"])

# Find missing codes

missing_codes = fund_codes - nav_codes

print("\nAMFI Code Validation:")

if len(missing_codes) == 0:
    print("✅ All AMFI codes are valid.")

else:
    print("❌ Missing AMFI codes:")
    print(missing_codes)

    print("\n===== DATA QUALITY SUMMARY =====")

# Missing values

print("\nMissing Values:")

print(fund_master.isnull().sum())

# Duplicate rows

print("\nDuplicate Rows:")

print(fund_master.duplicated().sum())

# Unique counts

print("\nUnique Counts:")

print("Fund Houses:", fund_master["fund_house"].nunique())

print("Categories:", fund_master["category"].nunique())

print("Sub Categories:", fund_master["sub_category"].nunique())

print("Risk Categories:", fund_master["risk_category"].nunique())