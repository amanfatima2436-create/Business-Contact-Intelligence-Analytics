import pandas as pd


def standardize_column_names(df):
    """
    Convert column names to snake_case.
    """

    print("Standardizing column names...")

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    return df


def clean_phone_numbers(df):
    """
    Clean and standardize phone numbers.
    """

    print("Cleaning phone numbers...")

    # Convert phone numbers to numeric values
    df["phone_number"] = pd.to_numeric(
        df["phone_number"],
        errors="coerce"
    )

    df["phone_number"] = df["phone_number"].apply(
    lambda x: str(int(x)) if pd.notna(x) else pd.NA
)

    # Make sure all phone numbers are stored as strings
    df["phone_number"] = df["phone_number"].astype("string")

    # Correct verified incorrect phone numbers
    df.loc[
        df["law_firms_name"] == "Eversheds Sutherland (US) LLP",
        "phone_number"
    ] = "+17134706100"

    df.loc[
        df["law_firms_name"] == "Scarlett Law Group",
        "phone_number"
    ] = "+14153526264"

    return df


def clean_data(df):
    """
    Clean the raw dataset and prepare it for analysis.
    """

    print("Cleaning dataset...")

    # Standardize column names
    df = standardize_column_names(df)

    # Clean phone numbers
    df = clean_phone_numbers(df)

    return df