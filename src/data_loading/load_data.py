import pandas as pd
from pathlib import Path


def load_data():
    """
    Load the raw Excel dataset.
    """

    print("Loading dataset...")

    file_path = Path("data/raw/Lead_Generation_Sample.xlsx")

    df = pd.read_excel(file_path)

    return df