from pathlib import Path
import pandas as pd

URL = ('https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/' +
       'e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx')

df = pd.read_excel(URL, skiprows=1, engine='openpyxl')

df['First Name'] = df['First Name'].str.strip()
df['Gender'] = df['Gender'].map({'Boy': 'Male', 'Girl': 'Female'})
df = df.rename(columns={'Ranking by Gender & Year': 'rank',
                        'First Name': 'babyname',
                        'Frequency': 'number',
                        'Year': 'year',
                        'Gender': 'sex'})

Path('alberta').mkdir(exist_ok=True)
df.to_csv('alberta/alberta-babynames.csv', index=False)
