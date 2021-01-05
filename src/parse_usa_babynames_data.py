import pandas as pd
from pathlib import Path

for f in Path('output').glob('*.html'):
    filepath = str(f)
    year = f.stem
    print(year)
    tables_list = pd.read_html(filepath)
    df = tables_list[2]
    df['year'] = year
    df = df[~df['Rank'].str.startswith('Note')]
    df.to_csv(f.with_suffix('.csv'), index=False)


#tables = [pd.read_html(str(f))[2].assign(year=f.stem) for f in Path('output').glob('*.html')]
