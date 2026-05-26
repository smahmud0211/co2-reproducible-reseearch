.PHONY: install run clean

install:
	pip install -r requirements.txt

run:
	python3 src/co2_analysis/main.py

clean:
	rm -rf outputs/figures/*.png
	rm -rf src/co2_analysis/__pycache__