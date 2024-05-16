# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:30:57 2023

@author: Paresh Dhamne

PROBLEM STATEMENT:
    Perform K means clustering on the airlines dataset to obtain optimum number of clusters. 
    Draw the inferences from the clusters obtained. Refer to EastWestAirlines.xlsx dataset.


Business Objective:
minimize:Customer dissatisfaction and churn rates by identifying and addressing pain points in services.
maximize: Revenue from additional services such as frequent flyer programs, premium seat bookings, and ancillary services.

Business Constraints:
                 Regulatory compliance with safety standards and industry regulations.
                 

DATA DICTIONARY
'''
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
                 
"""

#######################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_excel("D:/Datasets/EastWestAirlines.xlsx")
df

########################################################################
#EDA
#columns present in dataset
df.columns
'''
Out[7]: 
Index(['ID#', 'Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'Days_since_enroll', 'Award?'],
      dtype='object')
'''
#########################################################################

#display number of rows and columns
df.shape
#Out[8]: (3999, 12)

#5 number summary
df.describe()
'''
Out[9]: 
               ID#       Balance  ...  Days_since_enroll       Award?
count  3999.000000  3.999000e+03  ...         3999.00000  3999.000000
mean   2014.819455  7.360133e+04  ...         4118.55939     0.370343
std    1160.764358  1.007757e+05  ...         2065.13454     0.482957
min       1.000000  0.000000e+00  ...            2.00000     0.000000
25%    1010.500000  1.852750e+04  ...         2330.00000     0.000000
50%    2016.000000  4.309700e+04  ...         4096.00000     0.000000
75%    3020.500000  9.240400e+04  ...         5790.50000     1.000000
max    4021.000000  1.704838e+06  ...         8296.00000     1.000000

[8 rows x 12 columns]
'''
##########################################################################

#In dataset ID# and Award? are not important so drop it

df1=df.drop(['ID#','Award?'],axis=1)

df1.columns
'''
Out[11]: 
Index(['Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'Days_since_enroll'],
      dtype='object')
'''
##########################################################################

#display the number of rows and columns
df1.shape

#check any null values is there in dataset
df1.isnull().sum()
'''
Out[13]: 
Balance              0
Qual_miles           0
cc1_miles            0
cc2_miles            0
cc3_miles            0
Bonus_miles          0
Bonus_trans          0
Flight_miles_12mo    0
Flight_trans_12      0
Days_since_enroll    0
dtype: int64
'''

##########################################################################

# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#now apply this normlization function to Univ dataframe gor all the rows

df_norm=norm_fun(df1.iloc[:,:])
#it will give us normalize value between 1 to 0

#######################################################################
TWSS=[]
k=list(range(1,10))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
TWSS
#as k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters");
plt.ylabel("Total_within_SS");

########################################################################
model=KMeans(n_clusters=3)

model.fit(df_norm)

model.labels_
#Out[19]: array([2, 2, 2, ..., 1, 0, 0])

mb=pd.Series(model.labels_)

#assign thsi series to df1 dataframe as column and name the column as "cluster
df1['clust']=mb

df1.head()
'''
Out[22]: 
   Balance  Qual_miles  cc1_miles  ...  Flight_trans_12  Days_since_enroll  clust
0    28143           0          1  ...                0               7000      2
1    19244           0          1  ...                0               6968      2
2    41354           0          1  ...                0               7034      2
3    14776           0          1  ...                0               6952      2
4    97752           0          4  ...                4               6935      1

[5 rows x 11 columns]
'''
####################################################################
#assign columns as sequence we want
df=df1.iloc[:,[3,1,2,4,5,6,7,8,9,10]]

df.iloc[:,2:].groupby(df.clust).mean()
'''
Out[24]: 
       cc1_miles  cc3_miles  ...  Days_since_enroll  clust
clust                        ...                          
0       1.110247   1.004947  ...        2185.879152    0.0
1       3.778092   1.024735  ...        4701.935689    1.0
2       1.128315   1.005988  ...        5751.805817    2.0

[3 rows x 8 columns]
#from the output cluster 2 has got highest Top 10
#lowest accept ratio,best faculty ratio and highest expenses
#highest graduates ratio
'''

########################################################################
df.to_csv('Kmeans_airlines.csv',encoding='utf-8')
import os
os.getcwd()    
########################################################################
'''
Benifits to the client:
    Performing K-means clustering on the airlines dataset helps identify distinct customer segments, 
    aiding in targeted strategies to minimize dissatisfaction and churn rates. Inferences drawn from 
    clusters enable the optimization of revenue from additional services while ensuring compliance with 
    safety standards and industry regulations.
'''
########################################################################


