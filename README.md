# CO2 Reproducible Research Project

This project reproduces and translates an existing R-based CO2 emissions analysis into Python.

Original R project:  
https://github.com/hoangsonww/CO2-Global-Emissions-Analysis

Dataset:  
https://github.com/owid/co2-data

## Project Goal

The goal is to reproduce the visualizations and analysis from the R project using Python, while making the workflow fully reproducible with:

•⁠  ⁠Python scripts and classes
•⁠  ⁠Docker
•⁠  ⁠Makefile
•⁠  ⁠clear documentation

## Project Structure

```text
data/raw/              Raw OWID CO2 dataset
reference/             Original R analysis
src/co2_analysis/      Python source code
outputs/figures/       Generated plots