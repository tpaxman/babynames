import pandas as pd
import numpy as np
import sys


def main():
    inputfile, outputfile = sys.argv[1:]
    df = pd.concat([get_gender_names_table(gender) for gender in ('Boys', 'Girls')])
    df = df.sort_values(['year', 'sex', 'rank'])
    df.to_csv(outputfile, index=False)


def get_gender_names_table(gender):
    df = pd.read_excel('downloads/uk-wales-babynames.xls', sheet_name=gender, skiprows=3)
    first_unwanted_row = df[df['Unnamed: 0'].isna()].index.min()
    df = df.rename(columns={'Unnamed: 0': 'babyname'}).set_index('babyname')
    level1 = pd.Series([np.nan if isinstance(x, str) else x for x in df.columns]).ffill().astype(int)
    level2 = df.iloc[0].values
    df.columns = pd.MultiIndex.from_arrays([level1, level2], names=('year', 'valuetype'))
    df = df.iloc[2:first_unwanted_row].copy()

    df = df.stack('year').reset_index().replace(':', 0)
    df['babyname'] = df['babyname'].astype(str)
    df['babyname'] = df['babyname'].str.title()
    df = df.rename(columns={'Count': 'number', 'Rank': 'rank'})
    df['sex'] = {'Boys': 'Male', 'Girls': 'Female'}.get(gender)
    return df


if __name__ == '__main__':
    main()
