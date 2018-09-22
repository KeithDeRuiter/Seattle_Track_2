# import dependencies

import os, io, requests, zipfile
#import itertools
#import datetime
import pandas as pd
#import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

#from geopy.distance import great_circle
plt.rcParams['figure.figsize'] = 10,6
import warnings
warnings.filterwarnings("ignore")

"""The data files are very large. It is normal for the download to take a few minutes"""

def download_ais_data(year, month, zone, data_dir='./data'):
    '''function to download ais data from https://marinecadastre.gov/ais/ 
    and return corresponding pandas dataframe'''
    
    # create data directory
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # create path to csv file
    csv_file = 'AIS_{}_{}_Zone{}.csv'.format(year, str(month).zfill(2), str(zone).zfill(2))
    csv_path = os.path.join(data_dir, 'AIS_ASCII_by_UTM_Month', str(year), csv_file)
        
    try:
        # read csv if already downloaded
        data = pd.read_csv(csv_path)
    except:
        # create zip file url
        zip_file_url = ('https://coast.noaa.gov/htdata/CMSP/AISDataHandler/'
                        '{}/AIS_{}_{}_Zone{}.zip'.format(year, year, 
                                                         str(month).zfill(2), 
                                                         str(zone).zfill(2)))
        # download and extract data
        r = requests.get(zip_file_url, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(data_dir)

        # load csv as dataframe
        data = pd.read_csv(csv_path)

    return data

df = download_ais_data(2017,6,11)
df.head()