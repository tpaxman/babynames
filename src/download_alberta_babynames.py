import io
from pathlib import Path
import pandas as pd
import requests
import openpyxl

URL = 'https://open.alberta.ca/dataset/11245675-b047-49fc-8bd1-cc2ce8314a6d/resource/e8aac308-c754-484c-b446-0c57ed0e8d37/download/baby-names-frequency.xlsx'
r = requests.get(URL)
with io.BytesIO(r.content) as f:
    wb = openpyxl.load_workbook(f)
df = pd.DataFrame(wb['Page1-1'].values)
df.columns = df.iloc[1, :].to_list()
df = df.drop(index=[0, 1])
df = df.rename(columns={'Ranking by Gender & Year': 'rank',
                        'First Name': 'babyname',
                        'Frequency': 'number',
                        'Year': 'year'})
df['sex'] = df['Gender'].map({'Boy': 'Male', 'Girl': 'Female'})
df = df.drop(columns='Gender')
df['babyname'] = df['babyname'].str.strip()

Path('alberta').mkdir(exist_ok=True)
df.to_csv('alberta/alberta-babynames.csv', index=False)
