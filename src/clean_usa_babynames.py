"""
see: https://www.ssa.gov/oact/babynames/limits.html
"""

# TERRITORY
import sys
import pathlib
import zipfile
import pandas as pd


def main():
    inputfile, outputfile, keyword = sys.argv[1:]
    tempdir = pathlib.Path(inputfile).parent / f'temp-usa-{keyword}-babynames'
    with zipfile.ZipFile(inputfile) as f:
        f.extractall(path=tempdir)

    def parse_file(x, keyword):
        if keyword in ('state', 'territory'):
            return pd.read_csv(x, names=[keyword, 'gender', 'year', 'babyname', 'number'])
        elif keyword == 'country':
            return pd.read_csv(x, names=['babyname', 'gender', 'number']).assign(year=x.stem[3:])

    df = pd.concat([parse_file(x, keyword) for x in tempdir.glob('*.txt')])
    df.to_csv(outputfile, index=False)


if __name__ == '__main__':
    main()
