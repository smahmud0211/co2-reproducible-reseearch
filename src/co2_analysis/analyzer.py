"""
Analysis utilities for the CO2 emissions project.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


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
            self.dataframe.groupby("year", as_index=False)["co2"]
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

    def gdp_co2_correlation(self) -> float:
        """
        Calculate correlation between GDP and CO2 emissions.
        """
        return self.dataframe["gdp"].corr(self.dataframe["co2"])

    def gdp_co2_regression(self) -> dict:
        """
        Fit a simple linear regression model predicting CO2 from GDP.
        """

        regression_data = self.dataframe[["gdp", "co2"]].dropna()

        x = regression_data[["gdp"]]
        y = regression_data["co2"]

        model = LinearRegression()
        model.fit(x, y)

        return {
            "coefficient": model.coef_[0],
            "intercept": model.intercept_,
            "r_squared": model.score(x, y),
        }


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
    print("GDP-CO2 correlation:", analyzer.gdp_co2_correlation())
    print("GDP-CO2 regression:", analyzer.gdp_co2_regression())
