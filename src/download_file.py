"""
Downloads a file from the internet
"""
import sys
import pathlib
import requests


def main():

    # read in source url and output filepath from command line
    output_file, source_url = sys.argv[1:]
    output_file = pathlib.Path(output_file)
    assert source_url.endswith(output_file.suffix), 'output file type does not match url file type'

    # create the output directory if needed
    output_file.parent.mkdir(exist_ok=True)

    # write the raw data to a file
    response = requests.get(source_url)
    with open(output_file, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    main()
