import sys
from pathlib import Path
import pandas as pd

inputfile, outputfile = sys.argv[1:]

df = pd.read_excel(inputfile, skiprows=1, engine='openpyxl')

df['First Name'] = df['First Name'].str.strip()
df['Gender'] = df['Gender'].map({'Boy': 'Male', 'Girl': 'Female'})
df = df.rename(columns={'Ranking by Gender & Year': 'rank',
                        'First Name': 'babyname',
                        'Frequency': 'number',
                        'Year': 'year',
                        'Gender': 'sex'})

Path(outputfile).parent.mkdir(exist_ok=True)
df.to_csv(outputfile, index=False)
