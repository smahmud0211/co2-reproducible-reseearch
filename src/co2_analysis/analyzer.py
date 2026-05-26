"""
Analysis utilities for the CO2 emissions project.
"""

import pandas as pd


class CO2Analyzer:
    """
    Performs basic analysis on cleaned CO2 emissions data.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def global_emissions_by_year(self) -> pd.DataFrame:
        """
        Calculate total global CO2 emissions by year.
        """
        return (
            self.dataframe
            .groupby("year", as_index=False)["co2"]
            .sum()
            .rename(columns={"co2": "total_co2"})
        )

    def top_emitters(self, year: int, n: int = 10) -> pd.DataFrame:
        """
        Return top CO2 emitting countries for a selected year.
        """
        return (
            self.dataframe[self.dataframe["year"] == year]
            .sort_values("co2", ascending=False)
            .head(n)
        )


if __name__ == "__main__":
    from data_loader import DataLoader
    from processor import DataProcessor

    loader = DataLoader("data/raw/owid-co2-data.csv")
    raw_data = loader.load_data()

    processor = DataProcessor(raw_data)
    clean_data = processor.remove_missing_values()

    analyzer = CO2Analyzer(clean_data)

    print(analyzer.global_emissions_by_year().head())
    print(analyzer.top_emitters(year=2022))