"""
Visualization utilities for the CO2 emissions project.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class CO2Visualizer:
    """
    Creates plots for CO2 emissions analysis.
    """

    def __init__(self, dataframe: pd.DataFrame, output_dir: str = "outputs/figures"):
        self.dataframe = dataframe
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def plot_global_emissions(self, global_data: pd.DataFrame) -> None:
        """
        Plot global CO2 emissions over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(global_data["year"], global_data["total_co2"])
        plt.xlabel("Year")
        plt.ylabel("Total CO2 emissions")
        plt.title("Global CO2 Emissions Over Time")
        plt.tight_layout()
        plt.savefig(self.output_dir / "global_co2_emissions.png")
        plt.close()

    def plot_top_emitters(self, top_emitters: pd.DataFrame, year: int) -> None:
        """
        Plot top CO2 emitting countries for a selected year.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(top_emitters["country"], top_emitters["co2"])
        plt.xlabel("Country")
        plt.ylabel("CO2 emissions")
        plt.title(f"Top CO2 Emitters in {year}")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(self.output_dir / f"top_emitters_{year}.png")
        plt.close()

    def plot_region_comparison(self, dataframe: pd.DataFrame) -> None:
        """
        Plot average CO2 emissions for EU vs Non-EU countries over time.
        """
        region_data = dataframe.groupby(["year", "region_group"], as_index=False)[
            "co2"
        ].mean()

        plt.figure(figsize=(10, 6))

        for group in region_data["region_group"].unique():
            subset = region_data[region_data["region_group"] == group]
            plt.plot(subset["year"], subset["co2"], label=group)

        plt.xlabel("Year")
        plt.ylabel("Average CO2 emissions")
        plt.title("EU vs Non-EU CO2 Emissions Over Time")
        plt.legend()
        plt.tight_layout()
        plt.savefig(self.output_dir / "eu_vs_non_eu_emissions.png")
        plt.close()
