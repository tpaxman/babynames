import pandas as pd
from pathlib import Path

df = pd.read_csv('alberta/alberta-babynames.csv')
totals = df.groupby(['year', 'sex'])['number'].sum().reset_index()
df2 = pd.merge(df, totals, suffixes=('', '_total'), on=['year', 'sex'])
df2['fraction'] = df2['number'] / df2['number_total']
df2.to_csv(f'alberta/alberta-babynames-percents.csv', index=False)

