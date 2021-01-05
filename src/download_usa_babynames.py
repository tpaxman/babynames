"""
Downloads the top 1000 baby names data from ssa.gov for 1880-2019
Outputs each data table as a raw html file
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from pathlib import Path

URL = 'https://www.ssa.gov/OACT/babynames/'
OUTPUT_FOLDER = 'output'
START_YEAR = 1880                             # earliest year available in the database
END_YEAR = 2019                               # most recent data available at the current time

# Create the output folder if it does not yet exist
Path(OUTPUT_FOLDER).mkdir(exist_ok=True)

# Navigate to the social security page for baby names
driver = webdriver.Chrome()
driver.get(URL)

# Specify seeing the Top 1000 births
select = Select(driver.find_element_by_id('rank'))
select.select_by_visible_text('Top 1000')

# Select the option to retrieve total number of births
driver.find_element_by_id('number').click()
driver.find_element_by_xpath('//*[@id="content"]/section[4]/div/div/div[1]/form/p[3]/input[1]').click()
sleep(2)

# For all valid years (1880-2019) retrieve the raw html data tables
for y in range(START_YEAR, END_YEAR + 1):

    year_string = str(y)

    # type the year into the input field
    elem = driver.find_element_by_id('yob')
    elem.clear()
    elem.send_keys(year_string)

    # Click the "Go" button
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[1]/form/input[4]").click()
    sleep(1)

    # Write raw html to a file
    with open(f'{OUTPUT_FOLDER}/{year_string}.html', 'w') as f:
        f.write(driver.page_source)