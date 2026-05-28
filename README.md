# CO2 Reproducible Research Project

This project reproduces and translates an existing R-based CO2 emissions analysis into Python.

## Original R Project

https://github.com/hoangsonww/CO2-Global-Emissions-Analysis

## Dataset

https://github.com/owid/co2-data

## Project Goal

The goal of this project is to reproduce the visualizations and statistical analyses from the original R project using Python while ensuring full computational reproducibility.

The workflow includes:

- structured Python scripts and classes
- Docker-based reproducible environment
- Makefile automation
- reproducible visualizations and statistical analysis
- clear project documentation

---

# Project Structure

```text
data/raw/              Raw OWID CO2 dataset
reference/             Original R analysis
src/co2_analysis/      Python source code
outputs/figures/       Generated plots
docs/                  Documentation
reports/               Final report
```

---

# Main Features

The project currently includes:

- global CO2 emissions analysis
- top CO2 emitting countries analysis
- EU vs Non-EU comparison
- GDP and CO2 correlation analysis
- GDP and CO2 linear regression analysis
- automated figure generation
- Docker reproducibility
- Makefile automation

---

# Generated Outputs

The pipeline generates:

- `global_co2_emissions.png`
- `top_emitters_2022.png`
- `eu_vs_non_eu_emissions.png`

---

# How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
make run
```

---

# How to Run with Docker

Build Docker image:

```bash
docker build -t co2-reproducible-research .
```

Run container:

```bash
docker run co2-reproducible-research
```

---

# Example Console Output

```text
Pipeline completed. Figures saved in outputs/figures/
GDP-CO2 correlation: 0.9657
GDP-CO2 regression: {
    'coefficient': 3.35e-10,
    'intercept': 28.61,
    'r_squared': 0.93
}
```

---

# Team Members

- Said Mahmud
- Sabir
- Aykhan
- Nural