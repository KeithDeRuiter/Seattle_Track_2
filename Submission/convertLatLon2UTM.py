# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 08:36:45 2018

@author: Sandy
"""

#convert lat lon to utm
#The return has the form (EASTING, NORTHING, ZONE NUMBER, ZONE LETTER)
import utm
def convertLatLon2UTM(df):
    utm.from_latlon(df['LAT'], df['LON'])
    return df
