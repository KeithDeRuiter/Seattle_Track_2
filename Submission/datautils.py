#!/usr/bin/env python

# To use the functions in this file, use the following command:
# e.g., import Submission.datautils as utils

import os
import io
import requests
import zipfile
import pathlib as p
import pandas as pd
from pandas import errors
import numpy as np
import matplotlib.pyplot as plt
from urllib import parse


def _get_csv(filename):
    csv = None
    if p.Path(filename).exists():
        try:
            csv = pd.read_csv(filename)
        except FileNotFoundError:
            csv = None
        except errors.ParserError:
            raise errors.ParserError("Found a file, but couldn't part AIS CSV!")
    return csv


def _download_file(url, local_dir=p.Path.cwd(), local_name=None):
    if local_name is None:
        local_name = p.Path(parse.urlparse(url).path).name
    local_file = p.Path(local_dir)
    local_file = local_file / local_name
    r = requests.get(url, stream=True)
    with open(local_file, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(local_file.resolve())
    if local_file.exists():
        return local_file.resolve()
    return None


def _extract_zip(filename, dir=p.Path.cwd()):
    if not zipfile.is_zipfile(filename):
        return None
    z = zipfile.ZipFile(p.Path(filename).resolve(), "r")
    z.extractall(dir)
    extracted_files = []
    for file in z.namelist():
        extracted_files.append(p.Path(dir, file))
    if not extracted_files:
        return None
    return extracted_files


def main():
    year = 2017
    month = 6
    zone = 11
    dir = p.Path(p.PurePath(__file__).parent) / ".." / "Data"

    base_string = "AIS_{}_{}_Zone{}".format(year, str(month).zfill(2), str(zone).zfill(2))
    filename = base_string + ".csv"
    filename = p.Path(dir / filename).resolve()

    df = _get_csv(filename)

    if df is None:
        url = "https://coast.noaa.gov/htdata/CMSP/AISDataHandler/{}/".format(year)
        url += base_string
        url += ".zip"
        df = _download_file(url, dir, base_string + ".zip")
        if df is not None:
            df = _get_csv(_extract_zip(df, dir)[0])
            if df is None:
                raise FileNotFoundError("Could not extract downloaded file!")

    return df


if __name__ == "__main__":
    print("Running main.")
    main()