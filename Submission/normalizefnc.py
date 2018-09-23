# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:28:47 2018

@author: Sandy
"""
# import dependencies

import os, io, requests, zipfile
#import itertools
#import datetime
import pandas as pd
import datetime as dt
#import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
#normalize dataset for LAT LON and BaseDateTime from 0 to 1
#need df to only contain LAT, LON, and BaseDateTime
def normalize01(df):
    (df-min(df))/(max(df)-min(df))
    return df

normalize01(df)