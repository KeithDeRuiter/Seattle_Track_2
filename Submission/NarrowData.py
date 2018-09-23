#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:22:35 2018

@author: janey
"""

import convertLatLon2UTM
import pandas as pd


def reduce_data(df):
    
    #remove all of the tug boat types from df
    tug_tows = [21,22,31,32,52,1023,1025] #VesselTypes that are actually tug boats
    df = df[~df.VesselType.isin(tug_tows)]
    
    #removes all of the ships that are not moving or invalid data
    not_moving = ['moored', 'at anchor', 'reserved for future use (9)', 'reserved for future use (13)']
    df = df[~df.Status.isin(not_moving)]
    
    #Finds every speed less than 0 and removes those from df
    speed_less_than_0 = df[df.SOG < 0]
    df = df[~df.SOG.isin(speed_less_than_0)]
    

    return df


#start = 1496275200.0

def four_hr_interval(input_frame, start_time):
    
    end_time = start_time + (4.0 * 60 * 60)
    four_hour_data = []
    
    for i in input_frame.ix[:, 'BaseDateTime']:
        if i < start_time or i > end_time:
            four_hour_data.append(i)
        
    
    input_frame = input_frame[~input_frame.BaseDateTime.isin(four_hour_data)]
            
    
    return input_frame





#interval is time in minutes
    

def get_interval_subset(input_frame, interval):
    start_time = input_frame.BaseDateTime.min()
    end_time = start_time + (interval * 60.0)
    BDT_max = input_frame.BaseDateTime.max()
    
    baseDateTime_subsetList = []
    df_intervalSubset_list = []
    
    while end_time <= BDT_max:
        baseDateTime_subsetList = input_frame[(input_frame['BaseDateTime']>= start_time) & (input_frame['BaseDateTime'] < end_time)]
        
        input_frame = input_frame[~input_frame.BaseDateTime.isin(baseDateTime_subsetList)]
        df_intervalSubset_list.append(input_frame)
        
        start_time = end_time
        end_time = start_time + (interval * 60.0)
        
    
    return df_intervalSubset_list




def mean_data_point(input_frame_list):
    
    
    mean_data_frame_list = []
    
    for data_frame in input_frame_list:
        #data_frame = convertLatLon2UTM(data_frame)
        output = pd.DataFrame({'MMSI': [], 'LAT': [], 'LON': []})
        for mmsi in data_frame['MMSI'].unique():
            ship_reports = data_frame[data_frame.MMSI == mmsi]
            lat_mean = ship_reports['LAT'].mean()
            lon_mean = ship_reports['LON'].mean()
            
            new = pd.DataFrame({'MMSI': [mmsi], 'LAT': [lat_mean], 'LON': [lon_mean]})
            output = pd.concat([output, new])
        
        mean_data_frame_list.append(output)
    
    
    return mean_data_frame_list
