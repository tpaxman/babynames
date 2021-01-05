import pandas as pd
from pathlib import Path
import re

for datavalue in ['number', 'percent']:
    for f in Path('output').glob(f'{datavalue}*.html'):
        filepath = str(f)
        year = re.sub(r'.*-(\d+)', r'\1', f.stem)
        print(year)
        tables_list = pd.read_html(filepath)
        df = tables_list[2]
        df['year'] = year
        df['value'] = datavalue
        df = df[~df['Rank'].str.startswith('Note')]
        df.to_csv(f.with_suffix('.csv'), index=False)

