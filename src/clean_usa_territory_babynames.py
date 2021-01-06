"""
Extracts all US baby names by territory data from ssa.gov for 1880-2019
see: https://www.ssa.gov/oact/babynames/limits.html
"""
import sys
import pathlib
import zipfile
import pandas as pd


def main():
    inputfile, outputfile = sys.argv[1:]

    tempdir = pathlib.Path(inputfile).parent / 'temp-usa-territory-babynames'
    with zipfile.ZipFile(inputfile) as f:
        f.extractall(path=tempdir)

    df = pd.concat([pd.read_csv(x, names=['territory', 'gender', 'year', 'babyname', 'number']).assign(territory=x.stem)
                    for x in tempdir.glob('*.txt')])

    df.to_csv(outputfile, index=False)


if __name__ == '__main__':
    main()
