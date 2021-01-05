import pandas as pd
from pathlib import Path

HEADERS = {
    'Rank': 'rank',
    'Male name': 'babyname',
    'Female name': 'babyname',
    'Number of males': 'number',
    'Number of females': 'number',
    'Percent oftotal males': 'percent',
    'Percent oftotal females': 'percent'
}

# get number data
num_raw = pd.concat([pd.read_csv(str(f)) for f in Path('output').glob('number*.csv')])
num_m = num_raw[['Rank', 'Male name', 'Number of males', 'year']].rename(columns=HEADERS).assign(sex='Male')
num_f = num_raw[['Rank', 'Female name', 'Number of females', 'year']].rename(columns=HEADERS).assign(sex='Female')
df_num = pd.concat([num_m, num_f])

# get percent data
pct_raw = pd.concat([pd.read_csv(str(f)) for f in Path('output').glob('percent*.csv')])
pct_m = pct_raw[['Rank', 'Male name', 'Percent oftotal males', 'year']].rename(columns=HEADERS).assign(sex='Male')
pct_f = pct_raw[['Rank', 'Female name', 'Percent oftotal females', 'year']].rename(columns=HEADERS).assign(sex='Female')
df_pct = pd.concat([pct_m, pct_f])

# combine number and percent data
df = pd.merge(df_num, df_pct, on=['rank', 'babyname', 'sex', 'year'])
df['fraction'] = df['percent'].str[:-1].astype(float) / 100
df = df[['year', 'sex', 'rank', 'babyname', 'number', 'fraction']]

df.to_csv('usa-babynames.csv', index=False)
