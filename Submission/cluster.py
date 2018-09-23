#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 15:04:30 2018

@author: keith
"""

from sklearn.cluster import AffinityPropagation
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
import os, io, requests, zipfile
import itertools
import datetime
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt




df_XYZ = df[['LAT','LON','BaseDateTime']]
df_XYZ_subset = df_XYZ[0:10000]

af = AffinityPropagation(preference=-10).fit(df_XYZ_subset)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Estimated number of clusters: %d' % n_clusters_)
#print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
#print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
#print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
#print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
#print("Adjusted Mutual Information: %0.3f" % metrics.adjusted_mutual_info_score(labels_true, labels))
#print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels, metric='sqeuclidean'))

#Merge labels with data
df_XYZ_subset['label'] = labels

#group_data = pd.merge(df_XYZ_subset, labels)

sns.pairplot(x_vars=["LON"], y_vars=["LAT"], data=df_XYZ_subset,  hue="VesselType", 
             size=8, plot_kws={'alpha':0.25})
plt.title("LAT/LONG positions of the vessels, colored by VesselType (All data)")
plt.show()


sns.pairplot(x_vars=["LON"], y_vars=["LAT"], data=df_XYZ_subset,  hue="label", 
             size=8, plot_kws={'alpha':0.25})
plt.title("LAT/LONG positions of the vessels, colored by VesselType (All data)")
plt.show()