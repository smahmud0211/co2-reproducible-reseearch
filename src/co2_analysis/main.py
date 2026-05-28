"""
Main pipeline for reproducing the CO2 emissions analysis.
"""

from data_loader import DataLoader
from processor import DataProcessor
from analyzer import CO2Analyzer
from visualizer import CO2Visualizer


def main() -> None:
    """
    Run the full CO2 analysis pipeline.
    """
    loader = DataLoader("data/raw/owid-co2-data.csv")
    raw_data = loader.load_data()

    processor = DataProcessor(raw_data)
    clean_data = processor.remove_missing_values()

    analyzer = CO2Analyzer(clean_data)
    global_data = analyzer.global_emissions_by_year()
    top_emitters = analyzer.top_emitters(year=2022)

    correlation = analyzer.gdp_co2_correlation()
    regression = analyzer.gdp_co2_regression()

    visualizer = CO2Visualizer(clean_data)
    visualizer.plot_global_emissions(global_data)
    visualizer.plot_top_emitters(top_emitters, year=2022)

    print("Pipeline completed. Figures saved in outputs/figures/")
    print(f"GDP-CO2 correlation: {correlation}")
    print(f"GDP-CO2 regression: {regression}")


if __name__ == "__main__":
    main()