#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 13:22:35 2018

@author: janey
"""

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


def four_hr_interval(df, start_time):
    
    end_time = start_time + (4.0 * 60 * 60)
    four_hour_data = []
    
    for i in df.ix[:, 'BaseDateTime']:
        if i < start_time or i > end_time:
            four_hour_data.append(i)
        
    
    df = df[~df.BaseDateTime.isin(four_hour_data)]
            
    
    return df