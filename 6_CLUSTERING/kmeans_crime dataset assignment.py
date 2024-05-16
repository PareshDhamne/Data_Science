# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:57:07 2023

@author: PARESH DHAMNE

PROBLEM STATEMENT:
    2.	Perform clustering for the crime data and identify the number of clusters           
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

###############################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("D:/Datasets/crime_data.csv")
df
###############################################################################

#EDA
#columns present in dataset
df.columns
#Out[27]: Index(['Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape'], dtype='object')
##############################################################################

#display number of rows and columns
df.shape
#Out[28]: (50, 5)
#############################################################################

#check any null values is there in dataset
df.isnull().sum()
'''
Out[29]: 
Unnamed: 0    0
Murder        0
Assault       0
UrbanPop      0
Rape          0
dtype: int64
'''
#############################################################################

#5 number summary
df.describe()
'''
Out[30]: 
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
#except 1st all columns are important so we are not dropping any column

#############################################################################

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows
df_norm=norm_fun(df.iloc[:,1:])
#it will give us normalize value between 1 to 0
############################################################################

TWSS=[]
k=list(range(1,6))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS
#as k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS");
#shows elbow graph for given dataset

############################################################################
model=KMeans(n_clusters=3)

model.fit(df_norm)

model.labels_
'''
Out[36]: 
array([1, 1, 1, 2, 1, 1, 2, 2, 1, 1, 2, 0, 1, 2, 0, 2, 0, 1, 0, 1, 2, 1,
       0, 1, 2, 0, 0, 1, 0, 2, 1, 1, 1, 0, 2, 2, 2, 2, 2, 1, 0, 1, 1, 2,
       0, 2, 2, 0, 0, 2])
'''
###########################################################################
mb=pd.Series(model.labels_)

#assign thsi series to df1 dataframe as column and name the column as "cluster
df['clust']=mb

df.head()
'''
Out[39]: 
   Unnamed: 0  Murder  Assault  UrbanPop  Rape  clust
0     Alabama    13.2      236        58  21.2      1
1      Alaska    10.0      263        48  44.5      1
2     Arizona     8.1      294        80  31.0      1
3    Arkansas     8.8      190        50  19.5      2
4  California     9.0      276        91  40.6      1
'''
############################################################################

#assign columns as sequence we want
df=df.iloc[:,[1,2,3,4,5]]

df.iloc[:,1:].groupby(df.clust).mean()
'''
Out[41]: 
          Assault   UrbanPop       Rape  clust
clust                                         
0       78.538462  52.076923  12.176923    0.0
1      259.315789  68.315789  29.215789    1.0
2      143.888889  72.333333  19.344444    2.0
'''
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
#######################################################################

df.to_csv('Kmeans_crime.csv',encoding='utf-8')
import os
os.getcwd()    
#######################################################################

'''
Benifits to the client:
    Performing clustering on crime data aids in targeted resource allocation and policy formulation, 
    enhancing efficiency and effectiveness in crime prevention strategies while ensuring legal and 
    ethical compliance.
'''
#########################################################################