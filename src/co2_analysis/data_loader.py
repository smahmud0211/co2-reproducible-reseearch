"""
Data loading utilities for the CO2 emissions project.
"""

import pandas as pd


class DataLoader:
    """
    Loads the OWID CO2 emissions dataset.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self) -> pd.DataFrame:
        """
        Load dataset from CSV file.

        Returns:
            pd.DataFrame: Loaded dataset.
        """
        df = pd.read_csv(self.filepath)
        return df


if __name__ == "__main__":
    loader = DataLoader("data/raw/owid-co2-data.csv")
    data = loader.load_data()

    print(data.head())
