import pandas as pd
import os

# Folders

raw_folder = "data/raw"

processed_folder = "data/processed"

os.makedirs(processed_folder, exist_ok=True)

# Read all files

files = os.listdir(raw_folder)

for file in files:

    if file.endswith(".csv"):

        print(f"\nProcessing {file}")

        path = os.path.join(raw_folder, file)

        df = pd.read_csv(path)

        # Remove duplicates

        df = df.drop_duplicates()

        # -------------------
        # 02_nav_history.csv
        # -------------------

        if file == "02_nav_history.csv":

            df["date"] = pd.to_datetime(
                df["date"],
                errors="coerce"
            )

            df = df.sort_values(
                ["amfi_code", "date"]
            )

            df["nav"] = df.groupby(
                "amfi_code"
            )["nav"].ffill()

            df = df[df["nav"] > 0]

        # --------------------------
        # 08_investor_transactions.csv
        # --------------------------

        elif file == "08_investor_transactions.csv":

            if "transaction_type" in df.columns:

                df["transaction_type"] = (
                    df["transaction_type"]
                    .str.strip()
                    .str.title()
                )

            if "amount" in df.columns:

                df = df[df["amount"] > 0]

            if "date" in df.columns:

                df["date"] = pd.to_datetime(
                    df["date"],
                    errors="coerce"
                )

        # ------------------------
        # 07_scheme_performance.csv
        # ------------------------

        elif file == "07_scheme_performance.csv":

            if "expense_ratio_pct" in df.columns:

                df = df[
                    (df["expense_ratio_pct"] >= 0.1)

                    &

                    (df["expense_ratio_pct"] <= 2.5)
                ]

        # Save cleaned file

        output_name = file.replace(
            ".csv",

            "_cleaned.csv"
        )

        output_path = os.path.join(

            processed_folder,

            output_name

        )

        df.to_csv(

            output_path,

            index=False

        )

        print(f"Saved {output_name}")

print("\nAll files cleaned successfully")