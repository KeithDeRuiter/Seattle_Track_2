#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:49:33 2018

@author: keith
"""

from DownloadAIS import download_ais_data
from NarrowData import reduce_data


#Read in all data
df_full = download_ais_data(2017,6,11)


#Change time to secs

df = timeToSecFromEpoch(df_full)

#Filter data by coarse criteria
df = reduce_data(df_full)


#Pass through cluster/spacetime thing

#Output frame of *Possible* interesting inrteractions




#if __name__ === "__main__":
#    main()

