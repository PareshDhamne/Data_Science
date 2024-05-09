# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:42:38 2023

@author: Paresh Dhamne

Problem:
     Perform clustering for the airlines data to obtain optimum number of clusters. 
     Draw the inferences from the clusters obtained. Refer to EastWestAirlines.xlsx dataset.

Business Objective:
    
    minimize:Customer dissatisfaction and churn rates by identifying and addressing pain points in services.
    
    maximize: Revenue from additional services such as frequent flyer programs, premium seat bookings, and ancillary services.

Business Constraints:
                 Regulatory compliance with safety standards and industry regulations.
"""
'''

DATA DICTIONARY:
ID#		                Unique ID
Topflight		      	Indicates whether flyer has attained elite "Topflight" status, 1 = yes, 0 = no
Balance		          	Number of miles eligible for award travel
Qual_miles	          	Number of miles counted as qualifying for Topflight status
cc1_miles		      	Has member earned miles with airline freq. flyer credit card in the past 12 months (1=Yes/0=No)?
cc2_miles		      	Has member earned miles with Rewards credit card in the past 12 months (1=Yes/0=No)?
cc3_miles		      	Has member earned miles with Small Business credit card in the past 12 months (1=Yes/0=No)?
Bonus_miles		      	Number of miles earned from non-flight bonus transactions in the past 12 months
Bonus_trans				Number of non-flight bonus transactions in the past 12 months
Flight_miles_12mo		Number of flight miles in the past 12 months
Flight_trans_12 	    Number of flight transactions in the past 12 months
Day_since_enroll        Date of enroll  for flight
Award?                  Number of awards won by flight
'''
##############################################################################
import pandas as pd
import matplotlib.pyplot as plt

#now import file from data sett and create a dataframe
df=pd.read_excel("D:/Datasets/EastWestAirlines.xlsx")
df.describe()
'''
Out[4]: 
               ID#       Balance  ...  Days_since_enroll       Award?
count  3999.000000  3.999000e+03  ...         3999.00000  3999.000000
mean   2014.819455  7.360133e+04  ...         4118.55939     0.370343
std    1160.764358  1.007757e+05  ...         2065.13454     0.482957
min       1.000000  0.000000e+00  ...            2.00000     0.000000
25%    1010.500000  1.852750e+04  ...         2330.00000     0.000000
50%    2016.000000  4.309700e+04  ...         4096.00000     0.000000
75%    3020.500000  9.240400e+04  ...         5790.50000     1.000000
max    4021.000000  1.704838e+06  ...         8296.00000     1.000000

It gives 5 number summary
'''
#############################################################################
#EDA
#columns present in dataset
df.columns
'''
Out[5]: 
Index(['ID#', 'Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'Days_since_enroll', 'Award?'],
      dtype='object')
'''
#############################################################################
#display number of rows and columns
df.shape
#Out[6]: (3999, 12)
#############################################################################

#check any null values is there in dataset
df.isnull()
#There is no null value in dataset
#############################################################################

#Rename column name 
df=df.rename(columns={'ID#':'ID','Award?':'Award'})

#we have one column 'award' which really not useful we will drop it
df1=df.drop(["ID","Award"],axis=1)

df1.head(16)
##############################################################################
#we know that there is scale difference among the columns, which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normalization function to df1 dataframe for first 15 rows
df_norm=norm_func(df1.iloc[:,:])
###############################################################################

#you can check the df_norm dataframe which is scaled between values from 0 to 1
#you can apply describe function to new dataframe
b=df_norm.describe()
b
##############################################################################

# plot dendrogram first
#now to create dendrogram we need to measure distance,

#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function  gives us hirerarchicsl or algorithmic clustering
#ref the help for linkage
z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8));
plt.title("Hirerchical Clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
##############################################################################

#applying agglomerative clustering choosing 3 as clusetrs
#from dendrogram
#whatever has been displayed in dendrogram is not clustering
#it is just showing number of possible clusters

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
#apply labels to the clusters

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

#assign thsi series to univ dataframe as column and name the column as "cluster
df1['clust']=cluster_labels

df=df1.iloc[:,[3,1,2,4,5,6,7,8,9,10]]

df.iloc[:,2:].groupby(df.clust).mean()

#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
#############################################################################

df.to_csv("Airlienes.csv",encoding='utf-8')
import os
os.getcwd()
############################################################################
'''
Benifit to the client:
    The client can optimize services and offerings, reducing dissatisfaction 
    and churn while maximizing revenue by targeting specific customer segments 
    identified through clustering analysis. This strategic approach enhances 
    customer satisfaction and loyalty, driving sustainable growth and profitability.
'''
#############################################################################