# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 10:41:45 2018

@author: Sandy
"""

#create a dataframe with just lat lon time
df2=df[['LAT', 'LON']]
df2.head()

import utm
def convertLatLon2UTM(dataframe):
    utm_POS = utm.from_latlon(dataframe['LAT'], dataframe['LON'])
    return utm_POS

convertLatLon2UTM(df2)
df3 = df2.head(1000)
df3.head()
df3.count()

#kd tree try 1
import numpy as np
tree = KDTree(df3, leaf_size=2)     
print(tree.query_radius(X[0], r=4, count_only=True))
ind = tree.query_radius(X[0], r=4)  
print(ind)  # indices of neighbors within distance 4

#kd tree
import numpy as np
from scipy.spatial import KDTree
from scipy import spatial

tree = spatial.KDTree(df3)

#how deep is the resulting r tree?
#tree height = ceil(log(n-#of points)/log(fixed#ofchildren-eg 9)) 

# import KMeans
from sklearn.cluster import KMeans
# create np array for data points
points = df3
# create kmeans object
kmeans = KMeans(n_clusters=4)
# fit kmeans object to data
kmeans.fit(points)
# print location of clusters learned by kmeans object
print(kmeans.cluster_centers_)
# save new clusters for chart
y_km = kmeans.fit_predict(points)
plt.scatter(points[y_km ==0,0], points[y_km == 0,1], s=100, c='red')
plt.scatter(points[y_km ==1,0], points[y_km == 1,1], s=100, c='black')
plt.scatter(points[y_km ==2,0], points[y_km == 2,1], s=100, c='blue')
plt.scatter(points[y_km ==3,0], points[y_km == 3,1], s=100, c='cyan')

# import hierarchical clustering libraries
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
# create dendrogram
dendrogram = sch.dendrogram(sch.linkage(points, method='ward'))
# create clusters
hc = AgglomerativeClustering(n_clusters=4, affinity = 'euclidean', linkage = 'ward')
# save clusters for chart
y_hc = hc.fit_predict(points)
plt.scatter(points[y_hc ==0,0], points[y_hc == 0,1], s=100, c='red')
plt.scatter(points[y_hc==1,0], points[y_hc == 1,1], s=100, c='black')
plt.scatter(points[y_hc ==2,0], points[y_hc == 2,1], s=100, c='blue')
plt.scatter(points[y_hc ==3,0], points[y_hc == 3,1], s=100, c='cyan')

#kmeans take 2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
%matplotlib inline
from sklearn import datasets
X = df2
#KMeans
km = KMeans(n_clusters=3)
km.fit(X)
km.predict(X)
labels = km.labels_
#Plotting
fig = plt.figure(1, figsize=(7,7))
ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
ax.scatter(X[:, 3], X[:, 0], X[:, 2],
          c=labels.astype(np.float), edgecolor="k", s=50)
ax.set_xlabel("lat")
ax.set_ylabel("lon")
ax.set_zlabel("time")
plt.title("K Means", fontsize=14)

#Gaussian Mixture Model
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
%matplotlib inline
from sklearn import datasets
#Iris Dataset
iris = datasets.load_iris()
X = iris.data
#Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
proba_lists = gmm.predict_proba(X)
#Plotting
colored_arrays = np.matrix(proba_lists)
colored_tuples = [tuple(i.tolist()[0]) for i in colored_arrays]
fig = plt.figure(1, figsize=(7,7))
ax = Axes3D(fig, rect=[0, 0, 0.95, 1], elev=48, azim=134)
ax.scatter(X[:, 3], X[:, 0], X[:, 2],
          c=colored_tuples, edgecolor="k", s=50)
ax.set_xlabel("lat width")
ax.set_ylabel("lon length")
ax.set_zlabel("time")
plt.title("Gaussian Mixture Model", fontsize=14)