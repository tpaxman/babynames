import pandas as pd
from pathlib import Path

df_raw = pd.concat([pd.read_csv(str(f)) for f in Path('output').glob('*.csv')])

df_m = (df_raw[['Rank', 'Male name', 'Number of males']]
        .rename(columns={'Rank': 'rank', 'Male name': 'babyname', 'Number of males': 'number'})
        .assign(gender='Male'))

df_f = (df_raw[['Rank', 'Female name', 'Number of females']]
        .rename(columns={'Rank': 'rank','Female name': 'babyname','Number of females': 'number'})
        .assign(gender='Female'))

df = pd.concat([df_m, df_f])

df.to_csv('usa-babynames.csv', index=False)
