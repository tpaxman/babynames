# https://www.ssa.gov/oact/babynames/limits.html

DOWNLOAD=python src/download_file.py

.PHONY : rawdata cleandata
cleandata : $(patsubst %,clean-data/%-babynames.csv,usa-country usa-state usa-territory alberta uk-wales)
rawdata : $(patsubst %,downloads/%-babynames.zip,usa-country usa-state usa-territory) downloads/uk-wales-babynames.xls downloads/alberta-babynames.xlsx

clean-data/alberta-babynames.csv : src/clean_alberta_babynames.py downloads/alberta-babynames.xlsx
	python $^ $@

clean-data/usa-%-babynames.csv : src/clean_usa_babynames.py downloads/usa-%-babynames.zip
	python $^ $@ $*

clean-data/uk-wales-babynames.csv : src/clean_uk_wales_babynames.py downloads/uk-wales-babynames.xls
	python $^ $@

downloads/alberta-babynames.xlsx :
	$(DOWNLOAD) $@ https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx

downloads/usa-country-babynames.zip :
	$(DOWNLOAD) $@ https://www.ssa.gov/oact/babynames/names.zip

downloads/usa-state-babynames.zip :
	$(DOWNLOAD) $@ https://www.ssa.gov/oact/babynames/state/namesbystate.zip

downloads/usa-territory-babynames.zip :
	$(DOWNLOAD) $@ https://www.ssa.gov/oact/babynames/territory/namesbyterritory.zip

downloads/uk-wales-babynames.xls :
	$(DOWNLOAD) $@ https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesinenglandandwalesfrom1996%2fcurrent/babynames1996to2019.xls