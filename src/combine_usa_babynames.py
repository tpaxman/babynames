import pandas as pd
from pathlib import Path


# get number data
df_num_raw = pd.concat([pd.read_csv(str(f)) for f in Path('output').glob('number*.csv')])

df_num_m = (df_num_raw[['Rank', 'Male name', 'Number of males', 'year']]
            .rename(columns={'Rank': 'rank', 'Male name': 'babyname', 'Number of males': 'number'})
            .assign(gender='Male'))

df_num_f = (df_num_raw[['Rank', 'Female name', 'Number of females', 'year']]
            .rename(columns={'Rank': 'rank','Female name': 'babyname','Number of females': 'number'})
            .assign(gender='Female'))

df_num = pd.concat([df_num_m, df_num_f])


# get percent data
df_pct_raw = pd.concat([pd.read_csv(str(f)) for f in Path('output').glob('percent*.csv')])

df_pct_m = (df_pct_raw[['Rank', 'Male name', 'Percent oftotal males', 'year']]
            .rename(columns={'Rank': 'rank', 'Male name': 'babyname', 'Percent oftotal males': 'percent'})
            .assign(gender='Male'))

df_pct_f = (df_pct_raw[['Rank', 'Female name', 'Percent oftotal females', 'year']]
            .rename(columns={'Rank': 'rank','Female name': 'babyname','Percent oftotal females': 'percent'})
            .assign(gender='Female'))

df_pct = pd.concat([df_pct_m, df_pct_f])


# combine number and percent data
df = pd.merge(df_num, df_pct, on=['rank', 'babyname', 'gender', 'year'])


df.to_csv('usa-babynames.csv', index=False)
