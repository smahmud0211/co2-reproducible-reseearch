.PHONY: install run report all clean

install:
	pip install -r requirements.txt

run:
	PYTHONPATH=src python3 src/co2_analysis/main.py

report:
	PYTHONPATH=src python3 -m jupyter nbconvert --to html --execute reports/final_report.ipynb --output final_report.html

all: run report

clean:
	rm -rf outputs/figures/*.png
	rm -rf src/co2_analysis/__pycache__
	rm -f reports/final_report.html