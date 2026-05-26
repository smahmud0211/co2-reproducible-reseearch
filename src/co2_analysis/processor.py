"""
Data processing utilities for the CO2 emissions project.
"""

import pandas as pd


class DataProcessor:
    """
    Processes and cleans CO2 emissions data.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def select_columns(self) -> pd.DataFrame:
        """
        Select important columns for analysis.
        """
        columns = [
            "country",
            "year",
            "co2",
            "co2_per_capita",
            "gdp",
            "population"
        ]

        df = self.dataframe[columns]
        return df

    def remove_missing_values(self) -> pd.DataFrame:
        """
        Remove rows with missing values.
        """
        df = self.select_columns()
        df = df.dropna()

        return df


if __name__ == "__main__":
    from data_loader import DataLoader

    loader = DataLoader("data/raw/owid-co2-data.csv")
    data = loader.load_data()

    processor = DataProcessor(data)

    cleaned_data = processor.remove_missing_values()

    print(cleaned_data.head())
    print(cleaned_data.shape)