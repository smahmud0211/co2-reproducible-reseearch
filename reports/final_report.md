# Final Report

## Project Overview

This project reproduces and translates an existing R-based CO2 emissions analysis into Python using the Our World in Data CO2 dataset.

Original R project:
https://github.com/hoangsonww/CO2-Global-Emissions-Analysis

Dataset:
https://github.com/owid/co2-data

---

# Objectives

The main objectives of the project were:

- reproduce visualizations from the original R project
- reproduce statistical analysis in Python
- create a fully reproducible workflow
- use Docker for environment reproducibility
- automate execution using Makefile

---

# Reproduced Analyses

The project currently reproduces:

- global CO2 emissions over time
- top CO2 emitting countries
- GDP and CO2 correlation analysis
- GDP and CO2 linear regression analysis

---

# Extension

As an extension to the original R project, we introduced:

- EU vs Non-EU country classification
- comparison of average CO2 emissions between EU and Non-EU countries

---

# Reproducibility Features

The project includes:

- structured Python package
- Docker container
- Makefile automation
- Git version control
- reproducible outputs and figures

---

# Results

The analysis shows:

- strong positive correlation between GDP and CO2 emissions
- major differences between EU and Non-EU emission trends
- reproducible outputs between local and Docker environments

---

# Generated Figures

The pipeline generates:

- global_co2_emissions.png
- top_emitters_2022.png
- eu_vs_non_eu_emissions.png

---

# How to Run

## Local

```bash
pip install -r requirements.txt
make run
```

## Docker

```bash
docker build -t co2-reproducible-research .
docker run co2-reproducible-research
```