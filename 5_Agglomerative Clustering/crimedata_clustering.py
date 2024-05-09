# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:30:33 2023

@author: PARESH DHAMNE

Problem Statement:
    	Perform clustering for the crime data and identify the number of clusters
        formed and draw inferences. Refer to crime_data.csv dataset.

Business Objective:

Minimize: Crime rates in different regions or cities.

Maximize: Allocation of resources for crime prevention and law enforcement in high-risk areas.

Business Constraints:  
           Legal and ethical considerations regarding data privacy and surveillance.



Data Dictionary:

Murder -- Muder rates in different places of United States

Assualt- Assualt rate in different places of United States

UrbanPop - urban population in different places of United States

Rape - Rape rate in different places of United States
"""
##########################################################

import pandas as pd
import matplotlib.pyplot as plt
#########################################################

#now import file from data sett and create a dataframe
df=pd.read_csv("D:/Datasets/crime_data.csv")
a=df.describe()
a
'''
out[6]: 
         Murder     Assault   UrbanPop       Rape
count  50.00000   50.000000  50.000000  50.000000
mean    7.78800  170.760000  65.540000  21.232000
std     4.35551   83.337661  14.474763   9.366385
min     0.80000   45.000000  32.000000   7.300000
25%     4.07500  109.000000  54.500000  15.075000
50%     7.25000  159.000000  66.000000  20.100000
75%    11.25000  249.000000  77.750000  26.175000
max    17.40000  337.000000  91.000000  46.000000
'''
#########################################################

df1=df.head(14)

#########################################################

#we know that there is scale difference among the columns, which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x


#now apply this normalization function to df1 dataframe for first 13 rows
df_norm=norm_func(df1.iloc[:,1:])

############################################################

#you can check the df_norm dataframe which is scaled between values from 0 to 1
#you can apply describe function to new dataframe
b=df_norm.describe()
b
'''
Out[11]: 
          Murder    Assault   UrbanPop       Rape
count  14.000000  14.000000  14.000000  14.000000
mean    0.425193   0.553880   0.509967   0.436484
std     0.286671   0.283803   0.322818   0.307168
min     0.000000   0.000000   0.000000   0.000000
25%     0.244932   0.316609   0.244186   0.256737
50%     0.395270   0.614187   0.616279   0.344311
75%     0.520270   0.738754   0.744186   0.616018
max     1.000000   1.000000   1.000000   1.000000
'''
############################################################

# plot dendrogram first
#now to create dendrogram we need to measure distance,

#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function  gives us hirerarchicsl or Agglomotive clustering
#ref the help for linkage
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hirerchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
##########################################################

#applying agglomerative clustering choosing 3 as clusetrs from dendrogram

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
#apply labels to the clusters

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

#assign this series to univ dataframe as column and name the column as "cluster
df1['clust']=cluster_labels

df=df1.iloc[:,[1,2,3,4,5]]

df.iloc[:,1:].groupby(df.clust).mean()
'''
Out[22]: 
          Assault   UrbanPop       Rape  clust
clust                                         
0      136.166667  66.833333  16.966667    0.0
1      236.666667  55.333333  30.500000    1.0
2      271.600000  82.400000  33.240000    2.0
'''
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio

#######################################################################

df.to_csv("Crimedata.csv",encoding='utf-8')
import os
os.getcwd()
#####################################################################

'''
Benifit to the client:
    The clustering analysis on crime data allows the client to identify distinct patterns 
    in crime rates across different regions or cities, aiding in the allocation of resources 
    for crime prevention and law enforcement to high-risk areas.
'''
#######################################################################
