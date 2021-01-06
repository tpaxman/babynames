"""
Downloads the US baby names by state data from ssa.gov for 1880-2019
Outputs each data table as a raw html file

see: https://www.ssa.gov/oact/babynames/limits.html

"""
import io
import sys
import pathlib
import zipfile
import requests

def main():

    output_dir = sys.argv[1]
    unzip_from_url('https://www.ssa.gov/oact/babynames/state/namesbystate.zip', f'{output_dir}/usa-state')
    unzip_from_url('https://www.ssa.gov/oact/babynames/names.zip', f'{output_dir}/usa-country')


def unzip_from_url(url, dst):
    # create the output directory
    pathlib.Path(dst).mkdir(exist_ok=True)
    # get the zipfile data from the url
    response = requests.get(url)
    # extract the zipfile contents to the output directory
    with io.BytesIO(response.content) as f:
        zipfile.ZipFile(f).extractall(path=dst)


if __name__ == '__main__':
    main()
