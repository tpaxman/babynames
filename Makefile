
.PHONY : rawdata



clean-data/usa-state-babynames.csv
clean-data/usa-country-babynames.csv
clean-data/alberta-babynames.csv


rawdata :
	python src/download_file.py downloads/alberta-babynames.xlsx https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx
	python src/download_file.py downloads/usa-country-babynames.zip https://www.ssa.gov/oact/babynames/names.zip
	python src/download_file.py downloads/usa-state-babynames.zip https://www.ssa.gov/oact/babynames/state/namesbystate.zip
