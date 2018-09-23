# import dependencies

import os, io, requests, zipfile
#import itertools
import pandas as pd
import datetime as dt
import seaborn as sns
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
    
    print(data_dir)
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
        print("Couldn't find existing dataset.")
        # create zip file url
        zip_file_url = ('https://coast.noaa.gov/htdata/CMSP/AISDataHandler/'
                        '{}/AIS_{}_{}_Zone{}.zip'.format(year, year, 
                                                         str(month).zfill(2), 
                                                         str(zone).zfill(2)))
        # download and extract data
        print("downloading file")
        r = requests.get(zip_file_url, stream=True)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall(data_dir)

        # load csv as dataframe
        data = pd.read_csv(csv_path)

    return data


def timeToSecFromEpoch(dataframe):
    #Convert BaseDateTime to datetime
    dataframe.BaseDateTime = pd.to_datetime(dataframe.BaseDateTime, errors='raise') 
    dataframe['date'] = dataframe.BaseDateTime.apply(lambda x: x.date())
    
    #Subtract 1970 to convert to since epoch time
    dataframe.BaseDateTime = dataframe.BaseDateTime - dt.datetime(1970,1,1)

    #convert to seconds. All BasesDateTime should be seconds since epoch now
    dataframe.BaseDateTime = (dataframe.BaseDateTime.dt.total_seconds())
    
    return dataframe

def createLatLongDatePlot(dataframe):   
    sns.pairplot(x_vars=["LON"], y_vars=["LAT"], data=dataframe,  hue="BaseDateTime", size=6, plot_kws={'alpha':0.1})
    plt.title("LAT/LONG positions, colored by BaseDateTime ("+str(dataframe.BaseDateTime.values[0])+")")
    plt.show()

#ultraDf = download_ais_data(2017,6,11)













